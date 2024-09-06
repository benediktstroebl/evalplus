```python
def median(l: list):
    """Return median of elements in the list l."""
    return (sorted(l) + [0])[len(l) // 2]

# Test cases
test_median = [
    [(-10, 4, 6, 1000, 10, 20), -1, 0, float('inf')),
    # lis with only one element, or empty list
    ([1, 2, 4, 5]),
    # lis with all equal elements
    [1, 1, 1],
    # lis with large number of elements, and sorted, and shuffled copy
    [1, 2, 3, 4, 5, 6, 7], 20, 30]

def test_function(test_case):
    actual_result = median(test_case)
    expected_result = test_case[1]
    assert actual_result == expected_result, f"Test case {test_case} passed, but failed"

test_median.test_function(test_median)
 ```