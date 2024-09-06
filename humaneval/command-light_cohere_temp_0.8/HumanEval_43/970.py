```python
def pairs_sum_to_zero(lst):
    return any(x+y <= 0 for x,y in zip(lst, lst[1:]))

# Test the function with a variety of cases
for test_case in [[1, 3, 5], [1, 2, 3], [2, 4, -5], [1, 7], [1]]:
    actual = pairs_sum_to_zero(test_case)
    expected = [False, False, True, False, False]
    assert actual == expected, f"Test case {test_case} failed"
```  The above Python code provides a self-contained function `pairs_sum_to_zero` that determines whether two elements in an input list generate a sum that is less than or equal to zero. 

This function uses a simple "two-element test" to determine if the list contains two elements whose sum is zero. The test cases are provided to ensure the function's correctness with a variety of inputs.