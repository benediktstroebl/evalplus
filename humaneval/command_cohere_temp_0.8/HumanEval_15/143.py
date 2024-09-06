```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single argument, `n`, an integer representing the maximum number to be included in the sequence. The function uses the `range` function to generate a sequence of numbers from 0 to `n` (inclusive) using the `n+1` parameter. For each number in this sequence, the `map` function converts it to a string, and the `join` function concatenates these strings together, separated by spaces, to form the final string. 

The function's description also includes a docstring and a Markdown-style test suite with examples illustrating the function's behavior for different inputs. These examples show that the function returns a string containing a sequence of numbers from 0 to `n` separated by spaces, inclusive of `n`. 

For example, it returns `0` when `n` is 0, and it returns `0 1 2 3 4 5` when n is 5. These tests demonstrate the function's expected behavior and provide a clear understanding of how it should be used.