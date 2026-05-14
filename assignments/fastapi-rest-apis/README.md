# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a production-ready REST API using the FastAPI framework. You'll create a Todo application that demonstrates essential REST API concepts including request handling, data validation, and HTTP status codes.

## 📝 Tasks

### 🛠️ Task 1: Set Up Your First FastAPI Endpoint

#### Description
Initialize a FastAPI application and create your first GET endpoint. This task will familiarize you with the basic structure of a FastAPI application and how to define routes.

#### Requirements
Completed program should:

- Import and instantiate the FastAPI app
- Define a GET endpoint at `/` that returns a welcome message
- Define a GET endpoint at `/todos` that returns an empty list
- Run the server locally with uvicorn and verify it responds correctly

### 🛠️ Task 2: Add Data Validation with Pydantic Models

#### Description
Create a Pydantic model to represent Todo items and implement POST endpoint to create new todos. This demonstrates how FastAPI uses Pydantic for automatic request validation and serialization.

#### Requirements
Completed program should:

- Define a `Todo` Pydantic model with `id`, `title`, `description`, and `completed` fields
- Create a POST endpoint at `/todos` that accepts a Todo object
- Validate that required fields are provided and return appropriate error messages
- Store created todos in an in-memory list and return the created todo with a 201 status code

### 🛠️ Task 3: Implement CRUD Operations

#### Description
Build complete CRUD operations for the Todo API: create, read, update, and delete. This task demonstrates building a functional REST API following REST conventions.

#### Requirements
Completed program should:

- Implement GET `/todos/{todo_id}` to retrieve a specific todo by ID
- Implement PUT `/todos/{todo_id}` to update a specific todo
- Implement DELETE `/todos/{todo_id}` to delete a specific todo
- Return 404 status code when a todo is not found
- Return appropriate status codes (200, 201, 204, 404)

### 🛠️ Task 4: Add Query Parameters and Error Handling (Stretch Goal)

#### Description
Enhance the API with filtering and comprehensive error handling. This demonstrates advanced REST API patterns used in production applications.

#### Requirements
Completed program should:

- Add a query parameter to filter todos (e.g., by completion status)
- Implement custom error responses with descriptive messages
- Add request logging to track incoming requests
- Handle edge cases gracefully (empty lists, invalid IDs, malformed requests)
