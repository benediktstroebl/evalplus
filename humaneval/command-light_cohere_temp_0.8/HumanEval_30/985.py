```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Main code
if __name__ == "__main__":
    test_get_positive()
```
The code defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It uses list comprehension with the specific condition to filter out the positive numbers. The code then provides a test function to verify the correctness of the `get_positive` function. It uses the test function with a sample list and asserts that the returned list contains only the positive numbers. The code also contains the main code block, which demonstrates how to call the test function. The function is executed when the script is run.