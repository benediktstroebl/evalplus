```python
def pairs_sum_to_zero(l):
    """
    Check whether all pairs of elements in the list sum to zero.
    return True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    def test_sum_to_zero(test_list):
        return test_list and pairs_sum_to_zero(test_list)
    return test_sum_to_zero(test_list)

test_cases = [[1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 5, 7]]

for test in test_cases:
    print(test, '->', test_sum_to_zero(test))
```

The `test_sum_to_zero` function takes a list as input and checks if the function `pairs_sum_to_zero` would return `True` for the input list. The function returns `True` if the list contains two distinct elements that sum to zero, and `False` otherwise.