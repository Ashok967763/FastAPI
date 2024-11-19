# FastAPI Project Setup Guide

This document provides step-by-step instructions to set up and run the FastAPI project.

---

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.7 or later
- pip (Python package manager)

---

## Setup Instructions

1. **Create a Virtual Environment**  
   Open a terminal and navigate to your project directory. Run the following command to create a virtual environment:

   ```bash
   python -m venv fast-api-env

2. **Activate the Virtual Environment**
   ```bash
   fast-api-env\Scripts\activate.bat
3. ***Install FastAPI***
   ```bash
   pip install fastapi
4. ***Install Uvicorn***
   ```bash
   pip install "uvicorn[standard]"

## Running the Application
1. ***start the server***
   ```bash
   uvicorn main:app --reloads
