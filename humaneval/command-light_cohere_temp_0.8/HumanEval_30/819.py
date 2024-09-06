```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Tests
def test_get_positive():
    """Function tests"""
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

if __name__ == "__main__":
    # Function Execution
    print("Function Execution:", end="streamed")
    test_get_positive()
```
The script defines a function called get_positive that takes a list lst as input and returns a new list containing only the positive numbers from the original list. The function is tested using the test_get_positive function, which verifies the correctness of the get_positive function by passing different input lists and checking the resulting lists for containing only positive numbers.