```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'

test_string_sequence()
```

### Explanation:
- This code utilizes the `range()` generator to generate a sequence of numbers ranging from 0 to `n`.
- The `map()` function is then used to convert these numbers to strings, appending each to a list.
- `join()` is subsequently applied to turn the list of strings into a single string, separated by spaces. 

The `test_string_sequence()` function is used to verify the correctness of `string_sequence()`, ensuring that it returns the expected outputs for various inputs. 

The final `test_string_sequence()` call executes these tests, confirming the expected behavior of the `string_sequence` function. 

This solution is concise, adhering to Python best practices, and utilizes efficient built-in functionalities like `range()` and `map()` to achieve the desired result.