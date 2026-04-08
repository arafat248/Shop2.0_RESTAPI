from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .serializer import cart_serial, cartitem_serial, addcartitem_serial, up_da_serial, OrderSerial, CreateOrderSerial, UpdateOrderSerial
from .models import Cart, CartItem, OrderItem, Order
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class cart_view(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    #queryset = Cart.objects.all()
    serializer_class = cart_serial
    #permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)
    
    def get_queryset(self):
        return Cart.objects.filter(users = self.request.user)

class cart_item_view(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return addcartitem_serial
        elif self.request.method == 'PATCH':
            return up_da_serial
        return cartitem_serial
    
    def get_serializer_context(self):
        return{'cart_id' : self.kwargs['cart_pk']}
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])

class OrderViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'patch', 'option', 'head']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method=='POST':
            return CreateOrderSerial
        elif self.request.method == 'PATCH':
            return UpdateOrderSerial
        return OrderSerial
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

