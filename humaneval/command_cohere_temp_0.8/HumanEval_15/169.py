```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
print(string_sequence(0))   # Expected: 0
print(string_sequence(5))    # Expected: 0 1 2 3 4 5
``` 

This code snippet includes a function called `string_sequence` taking a single argument `n`, which is the total number of numbers needed in the sequence. The function uses the `range` function in conjunction with the `str` map function to convert the range of numbers into a string with each number separated by spaces. The number `n` is added to ensure the sequence is inclusive. 

The code also includes a set of tests to ensure the correct behavior of the function with different inputs. You can add these tests in a dedicated file named `test_string_sequence.py` to maintain code organization and adhere to good testing practices, as it is recommended to separate tests from code files.