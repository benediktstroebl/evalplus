```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single argument `n`, an integer denoting the maximum number to be included in the resultant string. Within this function, it utilizes the `range` function to generate a sequence of numbers ranging from 0 to `n` inclusive. Then, by employing the `join` method, it concatenates these numbers into a single string with spaces as separators. The resulting space-delimited number string is then returned. 

The function encapsulates the problem's essence: given a number `n`, produce a string that represents a sequence of numbers from 0 to `n` punctuated by spaces.