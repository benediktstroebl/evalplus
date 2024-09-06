```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This problem can be solved using the range function in Python which creates a sequence of numbers starting from 0 up to including n. Then, this sequence is converted into a string using the map and join functions. Lastly, the resulting string is returned as the answer to the problem. A usage example is displayed below:
```python
>>> string_sequence(0)
'0'
>>> string_sequence(5)
'0 1 2 3 4 5'
```