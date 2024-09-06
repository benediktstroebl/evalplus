```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Main function
if __name__ == "__main__":
    test_get_positive()
``` 
This script defines a `get_positive` function that takes a list l as input and returns a new list containing only the positive numbers from the original list. The `test_get_positive` function contains unit tests to ensure the correctness of the `get_positive` function.