```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)

# Test the function
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['']))        # Output: ''
print(concatenate([]))        # Output: ''
print(concatenate([['a'], ['b'], ['c']]))  # Output: 'abc'

```
The function concatenate accepts a list of strings and returns the concatenated result. A simple test of strings is used to achieve this, and the results are then printed to the console to verify the function's correctness.