```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single argument 'n', an integer representing the maximum number to be included in the sequence. The function leverages the `range` function to generate an array of numbers from 0 to 'n' inclusive, and the `join` method to concatenate these numbers into a single string with spaced-delimiters. 

The output accordingly corresponds to the requested string sequence, with numbers ranging from 0 to 'n' and including the specified number of increments. 

To test this script, a user can invoke the `string_sequence` function with various input values and verify the output against the expected pattern. 

For instance, letting `n` be 5, and executing the function would yield the following result:
```
'0 1 2 3 4 5'
```

Hence, the function is properly designed and operationalized to solve the problem at hand.