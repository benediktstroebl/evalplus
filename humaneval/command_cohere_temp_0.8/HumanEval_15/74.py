```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))   # Expected: 0
print(string_sequence(5))    # Expected: 0 1 2 3 4 5
``` 

This code defines a function called `string_sequence`, which takes an integer as an input and returns a string containing space-separated numbers ranging from 0 to the input value inclusive. The function uses the `range` function to generate a sequence of numbers from 0 to n and then uses the `join` method to concatenate these numbers into a single string with spaces as separators. 

The example usage and output demonstrate the function's behavior for the given input values.