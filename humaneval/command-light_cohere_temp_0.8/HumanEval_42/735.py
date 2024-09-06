```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

#Test case 1
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

#Test case 2
def test_incr_list2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

if __name__ == "__main__":
    test_incr_list()
    test_incr_list2()
```
This Python code defines a function called incr_list that takes a list l as input and returns a new list with elements incremented by 1. The test_incr_list function tests the incr_list function by passing in two different lists and asserting that the returned lists are equal. The code also includes a if statement to ensure that the script is run when it's imported as a module.

Note: You can uncomment the `if __name__ == "__main__":` line to run the test cases when the script is executed directly.