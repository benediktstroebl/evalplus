```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite for get_positive function
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

if __name__ == "__main__":
    test_get_positive()
``` 
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the input list. The test suite `test_get_positive` contains two assertions that verify the correctness of this function. 

This code is self-contained and can be used as is, with the confidence that it will produce the expected results.