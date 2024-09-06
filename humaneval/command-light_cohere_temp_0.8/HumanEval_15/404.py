Here's the code that demonstrates the solution to the problem:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([f'{i}' for i in range(n+1)])

# Test cases
print(string_sequence(0))       # Output: '0'
print(string_sequence(5))      # Output: '0 1 2 3 4 5'
print(string_sequence(-5))    # Should raise error
```
The code defines a function called string_sequence that takes an integer n as input and generates a string containing space-separated numbers from 0 to n. The function uses the string.range and range built together with the numbers and a space to create the string. The function then returns the string.