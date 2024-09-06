```python
def median(lst):
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    return (lst[-1] + lst[len(lst) // 2]) / 2

# Test cases
for test_case in [
    [-10, 4, 6, 1000],
    [1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5],
    [20, 30, 40],
    [5, 6, 7, 8, 9, 10]
]:
    try:
        result = median(test_case)
        assert result == (5 + 3) / 2  # Test 1
        assert median([x for x in test_case if x != 5]) == 5  # Test 2
        assert median([x for x in test_case if x != 8]) == 8  # Test 3
        assert median([x for x in test_case]) == 5  # Test 4
        assert median([x for x in test_case]) == 6  # Test 5
        assert median([2, 4, 6]) == 6  # Test 6
        break
except Exception as e:
    print(f"Error occurred: {e}")
```
The function median is defined to calculate the median of the elements in the list lst. The median is calculated by finding the median of the odd elements and then the median of the even elements, and then taking the average of these two medians. 
Test cases are provided to ensure that the function is working correctly.