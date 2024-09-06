```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite
def test_get_positive():
    assert get_positive([1, 2, -3, 4]) == [1, 2, 3, 4]
    assert get_positive([-1, -5, -9]) == [-1, -9]
    assert get_positive([-1, 0, -4, -100]) == [-1, 0, -100]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123]) == [5, 3, 2, 3, 9, 123]
    assert get_positive([]) == []
test_get_positive()
``` 
This function, get_positive, is designed to take a list as input and return a new list that only contains the positive numbers from the original list. It uses list comprehension to create a new list, filtering out the positive numbers from the input list. This function can be easily understood, and its correctness can be evaluated through various test cases.