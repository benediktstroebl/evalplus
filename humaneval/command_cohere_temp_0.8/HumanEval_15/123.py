```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = range(n+1)
    return ' '.join(map(str, numbers))

# Tests
print(string_sequence(0))
```
The function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) and then uses `map` and `join` to convert this sequence into a string with space-separated numbers.