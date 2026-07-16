**Docker Networking & Reverse Proxy**

Ecommerce shopmart application
=====================

In this project, I built a mini e-commerce application using a microservices architecture. The application has two backend services: a User Service and a Product Service. Instead of exposing each service directly to users, I used Nginx as a reverse proxy, which acts as a single entry point

This is the architecture
   
                        Client (Browser)
                              │
                    http://<EC2-Public-IP>
                              │
                              ▼
                  +-----------------------+
                  |        Nginx          |
                  |    Reverse Proxy      |
                  |      Port 80          |
                  +-----------+-----------+
                              │
                 ┌────────────┴────────────┐
                 │                         │
         /users request             /products request
                 │                         │
                 ▼                         ▼
      +-------------------+      +--------------------+
      |   User Service    |      |  Product Service   |
      | Flask Application |      | Flask Application  |
      | Internal Port 5001|      | Internal Port 5002 |
      +-------------------+      +--------------------+
                 │                         │
                 └──────── Docker Network ────────────┘


This is the folder structure i have used
shopmart-reverse-proxy/
│
├── docker-compose.yml
├── nginx/
│   └── nginx.conf
├── user-service/
└── product-service/

docker-compose.yml

oncw we run the docker compose up -d command

"This file starts all the containers together and creates a custom Docker network."

nginx:
This folder contains the Nginx configuration. It decides which backend service should receive each request.

user-service/

"This is a Flask application that displays the registered users

product-service/

"This is another Flask application that displays the product catalog."



Request Flow
============
User opens

http://<EC2-Public-IP>/users

        │

        ▼

Nginx receives request

        │

Checks nginx.conf

        │

Matches /users

        │

Forwards request

        │

User Service

        │

Flask renders HTML page

        │

Returns response

        │

Nginx sends response

        │

Browser displays User Page
