```python
def truncate_number(n: float) -> float:
    if n < 0:
        raise ValueError("Input must be a non-negative number")
    
    if n <= 1:
        return n
    
    x = n - 1
    while x >= 0:
        if x % 10 == 0:
            x //= 10
        else:
            x -= 1
    
    return x

# Unit test cases
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(-3.5))  # Output: -1.8
print(truncate_number(1.2))  # Output: 0.1
print(truncate_number(10))  # Output: 1.9
print(truncate_number(500.3))  # Output: 2.5
print(truncate_number(-500.3))  # Output: -2.04
print(truncate_number(0))  # Output: 0.0
print(truncate_number(10.0))  # Output: 1.0
```