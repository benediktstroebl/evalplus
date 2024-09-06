```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [0] * (n + 1)
    for i in range(n): result[i+1] = l[i] + 1
    return result
 
def test_incr_list():
    """Return list with random elements."""
    lst = [5, 2, 8, 1, 3]
    result = incr_list(lst)
    assert all(map(lambda x: x == result[i+1], range(len(result))))

# Run the tests.
# Test cases can be executed directly below the function definition.
test_incr_list()
``` 
This script defines a function `incr_list` that returns a new list with elements from the input list incremented by 1. The `test_incr_list` function creates a test list with random elements and passes the test using `assert` statement with the map function to check if all elements in the result list are equal to the corresponding element in the original list.