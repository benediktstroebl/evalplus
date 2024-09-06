```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base."""
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    return format(x, f"{base} ", ).replace(" ", "", 1)

# Example usage:
x = 8  # int 
base = 2  # int 

try: 
    result = change_base(x, base)
    print(result)
except ValueError as ve: 
    print(f"Error: {ve}")
```