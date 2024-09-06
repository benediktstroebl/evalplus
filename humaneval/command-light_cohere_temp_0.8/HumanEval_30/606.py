```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test case 1
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

#Test case 2
def test_get_positive2():
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

# Test case 3
def test_get_positive3():
    assert get_positive([9, 2, -3, -8, 4, 7, 5]) == [2, 3, 4, 9]

if __name__ == "__main__":
    # Run the tests
    test_get_positive()
    test_get_positive2()
    test_get_positive3()
```
The function `get_positive` takes a list as input and returns a new list containing only the positive numbers. The function uses a simple list comprehension to filter out the negative numbers from the input list.