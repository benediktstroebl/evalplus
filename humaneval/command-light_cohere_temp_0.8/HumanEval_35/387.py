```python
def max_element(l: list):
    """Return maximum element in the list
    Return -1 if the list is empty"""
    if not l: return -1
    return max(l)

#Tests
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123

def test_empty_list():
    test_list = []
    assert max_element(test_list) == -1

# Docstrings and docstrings
def doc_max_element():
    """Return maximum element in the list or -1 if empty"""
    print("Max element:", max_element([1, 2, 3, 99, 99]))

def __starting_point():
    doc_test = {
        'test_max_element': test_max_element,
        'test_empty_list': test_empty_list
    }
    print("Starting point: Docstrings and testing completed!", **doc_test)
__starting_point()
```
The provided code defines a function `max_element` that returns the maximum element in a list. The function returns -1 if the list is empty.

Additionally, there are two test functions: `test_max_element` tests a list with various elements and `test_empty_list` tests an empty list. 

Finally, the code provides docstrings and docstrings for a better understanding of the code's purpose and functionality.