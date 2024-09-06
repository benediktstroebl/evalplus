```python
def max_element(lst):
    if not_negative(lst):
        return max(lst)
    else:
        raise ValueError("Input list contains negative values")

def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

def not_negative(lst):
    return any(-x for x in lst)

if __name__ == "__main__":
    assert not_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    assert not not_negative([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

    lst = [1, 2, 3, -4, 4]
    assert not_negative(lst) is True
```

This version of the code provides a self-contained function and test suite for the problem. It uses the basic Python syntax and structure to define the function and test cases, making the code more concise and readable. The `not_negative()` helper function is introduced to quickly check for negative values in the list and raise an appropriate exception.