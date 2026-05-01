from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import user, project, task, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Team Task Manager")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "message": "TaskFlow API is running"}

app.include_router(user.router, prefix="/auth")
app.include_router(project.router, prefix="/projects")
app.include_router(task.router, prefix="/tasks")
app.include_router(dashboard.router, prefix="/dashboard")