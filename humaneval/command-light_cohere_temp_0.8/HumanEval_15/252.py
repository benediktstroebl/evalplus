Here's the corrected version of the Python script with self-contained functions:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n.

    '0'
   
    """ :count(n)"""
    return ''.join(str(i) for i in range(0, n+1))

def test_string_sequence(test_n: int) -> None:
    assert test_n == 0 or test_n == len('0'.join(str(i) for i in range(0, test_n+1)), "Test failed: unexpected end at position {}".format(test_n))
    assert test_n == len('0'.join(str(i) for i in range(0, test_n+1))[::-1], "Test failed: unexpected start at position {}".format(test_n))
    return

# Example usage
test_string_sequence(5)
```
This version is organized into functions with docstrings, which clearly describe their purpose, making it self-contained and easier to understand and maintain. The tests have also been refactored into separate functions with descriptive names, enhancing readability and reusability.