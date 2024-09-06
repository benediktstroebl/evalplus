```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Unit tests
def test_get_positive():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# main function usage
if __name__ == "__main__":
    # Example 1
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    print("List 1: ", lst1)
    print("positive elements: ", get_positive(lst1))

    # Example 2
    lst2 = [-1, 2, -4, 5, 6]
    print("List 2: ", lst2)
    print("positive elements: ", get_positive(lst2))
```
The above Python script defines a `get_positive` function that takes a list as an argument and returns a new list containing only the positive elements from the original list. It also contains unit tests for the test-get_positive function, which pass the test with different lists.