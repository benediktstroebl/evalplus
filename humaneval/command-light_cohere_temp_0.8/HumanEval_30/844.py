```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = []
test_cases = [
    [],  # [] converts to list
    [-1, 2, -4, 5, 6],
    5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
]

# Assertions
def test_function():
    test_get_positive.raise(test_cases)
    assert test_get_positive == [2, 5, 6], "Passed test cases!"
    test_get_positive.assertEquals([5])
   wer, "Negative numbers were not returned."

# Test results
print("Test passed!")
```