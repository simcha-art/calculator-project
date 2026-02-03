def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """פונקציית חילוק"""
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"