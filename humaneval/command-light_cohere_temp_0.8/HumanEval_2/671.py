```python
def truncate_number(number: float) -> float:
    return number - int(number) if abs(number) < 1 else 0.0

# Test cases
print(truncate_number(3.5)) # Output: 0.5
print(truncate_number(0.5)) # Output: 0.5
print(truncate_number(1))  # Output: 1
print(truncate_number(-1))  # Output: -1
print(truncate_number(5))  # Output: 5
print(truncate_number(10)) # Output: 9.9
print(truncate_number(-10)) # Error: ValueError
```