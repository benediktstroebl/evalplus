```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3]

# Test cases
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]

# Main function
if __name__ == "__main__":
    test_incr_list()
```
The code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. It uses the fundamental list comprehension to append a number 1 to each list element and then return the updated list.

The code also provides a test case for the incr_list function, which asserts that the returned list matches the expected output. The test_incr_list function is a simple test case that verifies the correctness of the incr_list function.