Here is a Python script that includes the function string_sequence that generates and returns a string of numbers from 0 up to the given n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([str(i) for i in range(n+1)])

# Example usage:
print(string_sequence(0)) # Output: 0
print(string_sequence(5)) # Output: 0 1 2 3 4 5 

```

This function utilizes a list comprehension to generate the string. It's a space-delimited representation of numbers from 0 up to n, inclusive. the function can be tested with the given test cases.