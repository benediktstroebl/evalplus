```python
def incr_list(lst):
    lst[::start:].append(1)
    for i, e in enumerate(lst[::start], start=1):
        lst[i].append(e + 1)
    return lst

def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(lst)
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert list(result) == expected, "Result does not match expected"

# Run the tests
test_incr_list()
```
This code defines a function `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The `test_incr_list` function contains a sample list and a result, and the expected result is also defined. The code then uses the specific test case to verify if the `incr_list` function correctly increments the elements of the list.

Finally, the code runs the `test_incr_list` function to execute the tests.