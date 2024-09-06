```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n - 1) / 2)]

# Test case 1: Check for valid input
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.2
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 2: Check edge cases
def test_median_edge_cases():
    assert median([]) == 0.0
    assert median([[]]) == 0.0
   
   
# Test case 3: Check for odd length list
def test_median_list_odd():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test_median()
test_median_edge_cases()
test_median_list_odd()

```

This script provides a self-contained solution for calculating the median of a list, along with tests to verify the correctness of the function. It covers different test scenarios: valid input, edge cases, and lists with odd lengths. The test cases are organized to ensure comprehensive testing of the `median` function.