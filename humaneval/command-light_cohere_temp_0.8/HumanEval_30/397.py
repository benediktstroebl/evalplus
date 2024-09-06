```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Tests
def test_get_positive():
    return all(get_positive([-1, 2, -4, 5, 6]))        # True

def test_get_positive_empty():
    return get_positive([]) == []          # True

def test_get_positive_single():
    return get_positive([5]) == [5]         # True

def test_get_positive_complex():
    return get_positive([3, -5, 9, -10]) == [3, 9]  # True

if __name__ == "__main__":
    print("Tests passed:")
    test_get_positive()
    test_get_positive_empty()
    test_get_positive_single()
    test_get_positive_complex()
```
This code defines a function `get_positive` that filters out negative numbers from an input list and returns a new list with only the positive numbers. The script also contains a series of test functions that verify the correctness of the `get_positive` function for various input scenarios. The `if __name__ == "__main__":` block ensures that the test code is executed only when the script is run directly, not when it's imported as a module.