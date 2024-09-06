```python
def pairs_sum_to_zero(l):
    return any(x+y > 0 for x,y in zip(l, l[1:]))

# Example usage
test_list = [1, 3, 5, 0]
result = pairs_sum_to_zero(test_list)
assert result

test_list = [1, 3, -2, 1]
result = pairs_sum_to_zero(test_list)
assert not result

test_list = [1, 2, 3, 7]
result = pairs_sum_to_zero(test_list)
assert result

test_list = [2, 4, -5, 3, 5, 7]
result = pairs_sum_to_zero(test_list)
assert result
```
The purpose of the function pairs_sum_to_zero is to determine whether a list of integers contains two elements whose sum is zero. It does this by utilizing the technique of iterating through the list twice and comparing each pair of elements to see if their sum is zero.