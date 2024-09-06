```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

# Test case 2
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]

# Test case 3 (Negative input)
try:
    assert get_positive([5, 3, -5, 2, -3, 3]) == [5, 3, 2]
    assert_failed()
except AssertionError as e:
    print(f"Error: {e}")

# Test case 4 (List of strings)
try:
    assert get_positive(["a", "b", "c"]) == ["a", "b", "c"]
    assert_failed()
except AssertionError as e:
    print(f"Error: {e}")
```

This script defines a `get_positive` function that takes a list as an argument and returns a new list containing only the positive elements from the original list. It also includes several test cases to verify the correctness of the function. The test cases cover various scenarios, including negative numbers, lists of strings, and a mix of numbers and non-positive elements.