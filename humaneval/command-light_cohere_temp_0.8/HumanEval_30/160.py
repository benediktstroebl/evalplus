```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = []
test_get_positive.py()
[-1, 2, -4, 5, 6]
test_get_positive.txt
[-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

# Function Test
def test_function():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Run the tests
test_get_positive.test()()

```