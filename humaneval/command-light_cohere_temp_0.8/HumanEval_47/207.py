```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list is empty.")
    if len(lst) == 1:
        return lst[0]
    m = len(lst) // 2 + 1
    mid1 = lst[m - 1]
    mid2 = lst[m]
    return (mid1 + mid2) / 2

# Test 1: Test with one element
test_median1 = [1]
result_median1 = median(test_median1)
assert result_median1 == 1

# Test 2: Test with two elements
test_median2 = [1, 2]
result_median2 = median(test_median2)
assert result_median2 == 2

# Test 3: Test with three elements
test_median3 = [1, 2, 3]
result_median3 = median(test_median3)
assert result_median3 == 2

# Test 4: Test with large list
test_median4 = [-10, 4, 6, 1000, 10, 20]
result_median4 = median(test_median4)
assert result_median4 == 15.0

# Test 5: Test error handling for empty list
try:
    median([])
except ValueError as e:
    print(f"Error: {e}")
``` 

The function median in this script accepts a list of numbers as input and determines the median value. The test section includes a variety of tests, including:

- **Test 1:** Single element list
- **Test 2:** List with two elements
- **Test 3:** List with three elements
- **Test 4:** List with a large number of elements
- **Test 5:** Empty list

The function also includes error handling for the case when the input list is empty, capturing the appropriate ValueError exception.