```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n + 1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

To validate the functionality, the `test_string_sequence` function is included, which employs the `string_sequence` function to run three test cases. The first test case uses `string_sequence(0)` as the input and the expected output is '0'. The second test case uses `string_sequence(5)` as the input and the expected output is '0 1 2 3 4 5'. The third test case uses `string_sequence(10)` as the input and the expected output is '0 1 2 3 4 5 6 7 8 9 10'. 

To execute the tests, the `test_string_sequence()` is called at the end of the script. 

This script can be executed independently and is self-contained, as it contains the function definition and the tests within the same file.  It can be evaluated by adding it to the codebase or by copying and pasting it into a Python interpreter.  As a result, it adequately addresses the problem statement in a self-contained manner.  If you have any more questions, please let me know!