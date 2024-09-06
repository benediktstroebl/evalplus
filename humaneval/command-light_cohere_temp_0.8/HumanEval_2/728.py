```python
def truncate_number(number: float) -> float:
    return 0.1 if number < 1 else:
        return number - 1 if number.1 < 0 else:
            return number - 0.5

# Test case
print(truncate_number(1.0)) # prints 0.1
print(truncate_number(0.9)) # prints 0.9
print(truncate_number(3.0)) # prints 2.0
print(truncate_number(-1.0)) # raises ValueError
```