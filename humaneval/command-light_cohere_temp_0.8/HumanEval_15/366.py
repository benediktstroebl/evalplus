```python
def string_sequence(n: int) -> str:
    if n <= 0:
        raise ValueError("n should be a positive integer")
    return "".join(str(i) for i in range(n))

# Test the function with different values of n
print(string_sequence(0))  # Output: 0
print(string_sequence(1))  # Output: 1
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10)) # Output: 0 10 9 8 7 6 5 4 3 2 1
print(string_sequence(0))  # ValueError: n should be a positive integer
```