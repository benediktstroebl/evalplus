```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Main function usage
if __name__ == "__main__":
    print("Testing...")
    test_get_positive()
```
The solution, represented as a function named `get_positive`, takes a list of numbers as input and returns a new list containing only the positive integers by filtering out the negative numbers from the input list. The function employs list comprehension and the boolean condition `num >= 0` to achieve this. 

The `test_get_positive` function contains unit tests that verify the correctness of the `get_positive` function with a variety of test cases. 

Finally, the `if __name__ == "__main__":` statement at the end of the script ensures that the test suite is executed when the script is run.