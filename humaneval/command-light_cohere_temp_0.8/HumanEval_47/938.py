```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        return None  # Handle empty list cases
    m = len(l) // 2 + 1
    if len(l) % 2 == 0:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]
# Test cases
for test_set in [[-10, 4, 6, 1000, 10, 20], [1, 2, 3, 4, 5, 6], [10, 20, 30, 40, 50], [1, 2, 3, 4, 6, 7], [10, -20, 30, 40, 50], [1, 2, 3, 4, 8, 9], [1, 4, 8, 16, 2, 8, 4, 2], [3, 4, 8, 2, 6, 8, 3], [1, 2, 4, 8, 2, 3, 4, 6, 7]]:
    actual_median = median(test_set)
    expected_median = [15.0, 15.0, 15.0, 15.0 for all made correctly
 results.

I hope this script provides a self-contained solution and passes all the test cases.