```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = []
test_get_positive.push([[-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 7, -9]])

def test_function():
    test_get_positive.pop(0)  # Removing empty test case
    return get_positive(test_get_positive)

if __name__ == "__main__":
    assert test_function() == [2, 5, 6, 3, 9, 123, 1]
```
This script defines a function get_positive that takes a list as input and returns a new list with only the positive numbers from the original list. It also includes a test suite with multiple test cases to ensure the correctness of the get_positive function.