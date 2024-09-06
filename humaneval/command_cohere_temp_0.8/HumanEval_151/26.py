```python
def double_the_difference(nums):
    odd_squares = sum(num**2 for num in nums if num % 2 and num >= 0 and isinstance(num, int))
    return int(odd_squares)
```

This function sums the squares of odd integers in the `nums` list after filtering out numbers that are negative, not integers, or both. It returns 0 if the list is empty. The condition `num >= 0` instead of `num > 0` ensures that the function correctly handles the case when the list contains the value 0. 

Here's a test case to ensure the function behaves correctly:
```python
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0 
assert double_the_difference([1, -1, 1, -1, 1]) == 18
assert double_the_difference([]) == 0
```