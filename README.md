# Shop248

Shop248 is a RESTful eCommerce backend API built with Django Rest Framework (DRF). It provides core eCommerce functionalities such as product management, category listing, cart handling, order processing, and secure user authentication.

The project uses JWT authentication with Djoser and includes API documentation with Swagger using drf_yasg.

## Features

- Product API
  - List all products
  - Retrieve single product details
  - Create, update, and delete products (admin access)

- Category API
  - List all categories
  - Retrieve category details
  - Manage categories (admin access)

- Cart API
  - Create shopping cart
  - Add products to cart
  - Update cart items
  - Remove cart items
  - View cart details

- Order API
  - Create order from cart
  - View order history
  - Manage orders

- Authentication
  - JWT authentication
  - User registration
  - Login / logout
  - Token refresh
  - Password reset support (Djoser)

- API Documentation
  - Swagger UI
  - ReDoc documentation

## Tech Stack

- Python
- Django
- Django Rest Framework
- Djoser
- Simple JWT
- drf_yasg
- SQLite / PostgreSQL (depending on configuration)

## Installation

### Clone the repository

```bash
git clone https://github.com/arafat248/Shop2.0_RESTAPI
cd shop248
```

### Create virtual environment

```bash
python -m venv env
```

Activate virtual environment:

Windows:

```bash
env\Scripts\activate
```

Mac/Linux:

```bash
source env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Run development server

```bash
python manage.py runserver
```

Server will run at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

Example endpoints:

```text
/api/products/
/api/categories/
/api/carts/
/api/orders/
/auth/jwt/create/
/auth/jwt/refresh/
```

## API Documentation

Swagger documentation:

```text
http://127.0.0.1:8000/swagger/
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc/
```

## Authentication

This project uses JWT authentication.

Get access token:

```http
POST /auth/jwt/create/
```

Refresh token:

```http
POST /auth/jwt/refresh/
```

Include token in request header:

```text
Authorization: Bearer <your_access_token>
```

## Project Structure

```text
Shop248/
├── products/
├── categories/
├── carts/
├── orders/
├── users/
├── manage.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Payment gateway integration
- Product reviews and ratings
- Wishlist feature
- Inventory management
- Discount and coupon system
- Email notifications

## License

This project is developed for learning and portfolio purposes.