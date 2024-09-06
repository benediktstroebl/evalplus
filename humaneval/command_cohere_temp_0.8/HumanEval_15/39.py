```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))

# Tests
print(string_sequence(0))   # Expected Output: 0
print(string_sequence(5))    # Expected Output: 0 1 2 3 4 5
```

This approach uses the map function to convert a range of numbers from 0 to n into a list of strings, and then joins these numbers into one string with spaces using the join function. 

For example, callings `string_sequence(5)` would return the string "0 1 2 3 4 5", which is the expected output for the given problem statement. 

The function also comes with a docstring and example usage that meets the requirement for the problem statement. 

Let me know if this solution suits your needs or if you'd like me to modify it in any way.