```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This problem can be solved using the range function in Python which creates a sequence of numbers starting from 0 up to n inclusive. Then, this sequence is converted into a string using the map and join functions. 

This approach results in the desired string containing all numbers from 0 to n formed as space-delimited sequence.