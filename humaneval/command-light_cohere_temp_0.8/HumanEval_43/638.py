```python
def pairs_sum_to_zero(l):
    return any(x + y == 0 for x, y in zip(l, l[1:]))

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
assert test_result == False

test_result = pairs_sum_to_zero([1, 3, -2, 1])
assert test_result == False

test_result = pairs_sum_to_zero([1, 2, 3, 7])
assert test_result == False

test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
assert test_result == True
```
The provided function, `pairs_sum_to_zero`, determines whether every element in a list pairs adds up to zero. It employs a using the `zip` function to iterate over the list's elements, comparing each pair's sum to zero.

The function returns `True` if any element doesn't add up to zero, indicating a pair of elements that sum to zero. Otherwise, it returns `False`. The test cases aim to cover various scenarios, including single elements, pairs without sum, and pairs with sum.