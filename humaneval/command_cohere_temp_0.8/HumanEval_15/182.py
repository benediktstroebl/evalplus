```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This problem can be solved using the range function in Python which creates a sequence of numbers starting from 0 up to n inclusive. Then, this sequence is converted into a string using the map and join functions. Lastly, the str function is used to convert each item in the sequence to a string. 

This approach gives the correct result for any integer value of n. And it does so without any explicit repetition of numbers, improving on the clarity and efficiency of the solution.