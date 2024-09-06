```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))
print(string_sequence(5))
```

This script includes a function called `string_sequence` which takes an integer `n` as input and returns a string consisting of space-separated numbers starting from 0 up to (and including) `n`. The function uses the `range` generator and maps it to a string using `str`, ensuring the numbers are spaced apart and separated by one or more spaces. The tests provided in the problem statement are also included in this script. 

When you run this script, it will output the following results, demonstrating that the function behaves as expected:
```
0
0 1 2 3 4 5
```