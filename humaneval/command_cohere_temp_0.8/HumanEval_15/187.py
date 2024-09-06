```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This version of the code uses Python's built-in `range` function to generate a sequence of numbers up to `n` and then maps these to strings using `map`, joining the results together with spaces using `join`. The output will be a string containing all numbers from 0 to `n` with a space in between. 

To test this script, you can call the function with a given `n` value and print the returned string. For example:
```python
print(string_sequence(0)) # Should print '0'
print(string_sequence(5)) # Should print '0 1 2 3 4 5'
``` 

This would help verify that the function produces the correct output for different values of `n`.  Such tests would ensure the correctness of the code and illustrate how the changed code achieves the desired result.