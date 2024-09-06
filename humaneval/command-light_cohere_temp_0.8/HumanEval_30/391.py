```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Tests
def test_get_positive():
    list1 = [-1, 2, -4, 5, 6]
    assert get_positive(list1) == [2, 5, 6]
    list2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert get_positive(list2) == [5, 3, 2, 3, 9, 123]

# Main method
if __name__ == "__main__":
    test_get_positive()
``` 
This code defines a `get_positive` function that takes in a list and returns a new list with only the positive numbers from the original list. 

The `test_get_positive` function contains a list with various numbers and utilizes the `get_positive` function to create a new list with only the positive numbers.