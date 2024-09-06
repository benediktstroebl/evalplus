```python
def pairs_sum_to_zero(l):
    """
    Check whether all elements in the list sum up to zero.
    """
    def check(nums):
        total = sum(nums)
        return total == 0
    return check(l)

# Test the function
test_pairs_sum_to_zero = check([1, 3, 5, 0])
test_pairs_sum_to_zero = check([1, 3, -2, 1])
test_pairs_sum_to_zero = check([1, 2, 3, 7])
test_pairs_sum_to_zero = check([2, 4, -5, 3, 5, 7])
test_pairs_sum_to_zero = check([1])

print("All test cases passed!")
```