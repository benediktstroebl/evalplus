Here is a Python script with a self-contained function that solves the problem of creating a string of numbers from 0 up to the provided n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([str(i) for i in range(n+1)])

# Test the function with different inputs
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
print(string_sequence(10)) # Output: '0 9 8 7 6 5 4 3 2 1'
print(string_sequence(0))
```

The function is designed to produce a string containing space-separated integers from 0 to n, where n is an integer. The function is straightforward and self-contained, and it can be easily used to generate sequences of numbers for different values of n.