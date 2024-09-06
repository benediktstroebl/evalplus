```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n.
    """
    return ' '.join(map(str, range(n + 1)))

# Tests
assert string_sequence(0) == '0'
assert string_sequence(5) == '0 1 2 3 4 5'
``` 

This code snippet solves the problem using a map function to convert a range of numbers from 0 to n to a string sequence. It also includes a test block to ensure the function behaves correctly for the given inputs. You can use it in your codebase and extend it with more comprehensive tests to cover edge cases and confirm the expected behavior.