```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test the function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
    return "Test passed"

# Call the function and print the result
result = test_incr_list()
print(result)
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The function is then tested using the test_incr_list, which checks if the function works correctly by comparing the output with the expected results. After the tests, the result is printed to the console.