```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test suite for function get_positive
tests = {
    "def test_positive():
        assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
        assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
        assert len(get_positive([10, -20])) == 1
        assert get_positive([0, 0]) == [0]
        assert get_positive([]) == []
        assert len(get_positive([10, 20, 30, 40, 50, 0, 0])) == 5
    }
```
The function get_positive takes a list as input and returns a new list with only the positive elements from the original list. 

The test suite contains several tests for different scenarios, such as lists with both positive and negative numbers, empty lists, and lists with zero elements.