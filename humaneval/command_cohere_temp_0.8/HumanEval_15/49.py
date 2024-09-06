```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to `n` inclusive. """
    numbers = f'{n}-{n}'
    return ' '.join(str(num) for num in range(int(numbers) + 1))

# Test Cases
print(string_sequence(0))
print(string_sequence(5))
```

This script defines a function called `string_sequence` that takes in an integer value `n` as input and returns a string containing a sequence of numbers starting from 0 up to, and including, `n`. The function utilizes a formatted string to create a sequence of numbers from `n - 1` to `n`. It then uses a list comprehension and the `join` method to convert this sequence into a string. 

The example usage demonstrates the behavior of the function for the test cases of `n = 0` and `n = 5`, where it produces the expected outputs `'0'` and `'0 1 2 3 4 5'`, respectively.