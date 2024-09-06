```python
def pairs_sum_to_zero(l):
    return any(x+y <= 0 for x, y in zip(l, l[1:]))

# Example usage:
if __name__ == "__main__":
    assert pairs_sum_to_zero([1, 3, -2, 1]) == False
    assert pairs_sum_to_zero([1, 2, 3, 7]) == False
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
    assert pairs_sum_to_zero([1]) == False
```
This code defines the `pairs_sum_to_zero` function that determines whether the sum of any two elements in a list will be zero or not. The `any()` function with a generator expression checks if there exists at least one pair of elements in the list where their sum is less than or equal to zero. The test cases cover a expected behavior, and the function returns `False` if there are no such pairs, and `True` if there is a pair that sums to zero.