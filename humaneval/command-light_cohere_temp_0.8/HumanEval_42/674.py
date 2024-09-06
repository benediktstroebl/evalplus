```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test function to check if the incr_list function works correctly
def test_incr_list():
    try:
        lst = [1, 2, 3]
        result = incr_list(lst)
        assert result == [2, 3, 4]
        result = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        assert result == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    except AssertionError as e:
        print(f"Error occurred: {e}")

# Driver code
test_incr_list()
```
The provided Python code defines a function incr_list that increments elements in a list by 1 and a separate test function test_incr_list that checks if the function works correctly with different inputs. The driver code runs the specific test cases to validate the behavior of the incr_list function.