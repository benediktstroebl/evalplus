```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))
```

The above code uses the `map` function to convert a range of numbers from 0 to n to a list of strings, and `join` joins these strings into one string with spaces in between. Since the range function produces numbers from 0 to n-1 by default, we add +1 to n to make the range inclusive of n. The example of usage printed in the output is:
```bash
0
```