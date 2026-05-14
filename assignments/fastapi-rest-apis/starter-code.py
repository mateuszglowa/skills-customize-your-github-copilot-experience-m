from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Todo API", version="1.0.0")

# TODO: Define your Pydantic model for Todo items here
# Should have: id (int), title (str), description (str), completed (bool)


# In-memory storage for todos (for this assignment, we'll use a simple list)
todos_db: List[dict] = []
next_id: int = 1


# TODO: Task 1 - Create your GET endpoints here
# - GET / should return a welcome message
# - GET /todos should return the list of todos


# TODO: Task 2 - Create POST endpoint here
# - POST /todos should accept a Todo object and add it to the database


# TODO: Task 3 - Implement CRUD operations here
# - GET /todos/{todo_id} to retrieve a specific todo
# - PUT /todos/{todo_id} to update a specific todo
# - DELETE /todos/{todo_id} to delete a specific todo


# TODO: Task 4 - Add query parameters and error handling (Stretch Goal)
# - Add query parameters to GET /todos for filtering
# - Implement custom error responses
# - Add request logging


if __name__ == "__main__":
    import uvicorn
    # Run the application with: uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
