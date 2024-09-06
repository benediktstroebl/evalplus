```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single argument, `n`, an integer representing the maximum number to be included in the sequence. The function utilizes the `range` function to generate an iterator of numbers from 0 to `n`, inclusive, and then uses the `str` function to convert each number to a string and the `join` function to concatenate these into a single string separated by spaces. 

The output produced by this function depends on the input `n`:
- If `n` is 0, the function returns a string '0', indicating a single-digit number. 
- If `n` is 5, the function returns the string '0 1 2 3 4 5', representing five space-separated numbers from 0 to 5. 

This function is designed to handle any positive integer input and can be used in various scenarios that require generating sequential numbers.