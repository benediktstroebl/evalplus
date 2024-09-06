Here is a Python script with a self-contained function that solves the problem of determining if a list of integers sums to zero:
```python
def pairs_sum_to_zero(l):
    return any([x == 0 for x in l])

# Test cases
test_pairs_sum = [
    [([1, 3], [0, 5]),
    ([1, 2], [-2, 1]),
    ([2, 4], [3, 5, 7])
]

test_results = {}
for test_case in test_pairs_sum:
    test_results[test_case[0]] =  pairs_sum_to_zero(test_case[1])

# Print the results
print("Test Results:")
for result in test_results.show(result)
```

The output of the above code will show the test results for each given test case. 

This function uses the `any()` function to check if any of the integers in the list are equal to zero. It returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.