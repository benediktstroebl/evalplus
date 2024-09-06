```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single integer argument and outputs a string containing all the numbers up to and including the provided integer. It leverages the `range` function to generate an array of numbers from 0 to `n` and then uses the `map` function to convert these numbers to strings, eventually joining them together into one string with spaces as separators via the `join` method.

Here's an example usage of this function to illustrate its behavior:
```python
print(string_sequence(5))  # Outputs: 0 1 2 3 4 5
```

This will print a string containing the numbers from 0 to 5, demonstrating the function's ability to generate a sequence of numbers up to a given input.