```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
```
The function 'string_sequence' takes an integer 'n' as input and returns a string consisting of space-separated numbers ranging from 0 to 'n' inclusively. It uses the 'range' function to generate a sequence of numbers from 0 to 'n' and then maps each number to a string using the 'str' function. These strings are then joined together with spaces using the 'join' method to produce the final result.