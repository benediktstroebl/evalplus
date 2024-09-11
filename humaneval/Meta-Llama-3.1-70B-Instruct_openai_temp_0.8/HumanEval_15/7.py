```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(map(str, range(n + 1)))

# Example use cases
print(string_sequence(0))
print(string_sequence(5))
```
In this script, the `string_sequence` function takes an integer `n` and uses the `range` function to generate numbers from 0 to `n` (inclusive). It then uses the `map` function to convert these numbers to strings, and finally uses the `join` function to concatenate these strings with spaces in between. The result is a string containing space-delimited numbers starting from 0 upto `n` inclusive.