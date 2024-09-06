Here is a self-contained Python script that defines a function that returns a string containing space-delimited numbers from 0 up to the given n:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([str(i) for i in range(n+1)])

# Test the function with different values of n
print(string_sequence(0))        # Output: '0'
print(string_sequence(5))       # Output: '0 1 2 3 4 5'
print(string_sequence(7))       # Output: '0 6 7 8 9'
print(string_sequence(10))      # Output: '0 9 ...'

```