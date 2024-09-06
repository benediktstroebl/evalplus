```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n+1)))
```

This script defines a function `string_sequence(n)` that returns a string consisting of space-separated numbers starting from 0 up to and including `n`. The `range(n+1)` function generates a sequence of numbers from 0 to `n` (inclusive), and the `map(str, range(n+1))` function converts each number in the sequence to a string. Finally, the `join()` method concatenates the string values together to form the final result. 

Here is an example usage of the function:
```python
print(string_sequence(5))  # Output: "0 1 2 3 4 5"
```

The output of this code will be "0 1 2 3 4 5" because it is a string sequence of numbers from 0 to 5 inclusive.