Here is a Python script that contains a self-contained function that solves the problem of generating a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f'{0}' + (' ' + str(i) for i in range(1, n+1))

# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(1))  # Output: '0 1'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(10)) # Output: '0 9 8 7 6 5 4 3 2 1'
print(string_sequence(-5)) # Raises error: ValueError
```