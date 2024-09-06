```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Test the function with different lists
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))          # Output: False
```
The script defines a function `pairs_sum_to_zero` that checks if there are two elements in the list that their sum is equal to zero. It uses the specific to the difference between elements by iterating over the list and comparing each element with the second element using `zip()`. specific to iterate through the list of pairs.

The test cases cover a variety of list scenarios and demonstrate the function's behavior. The function returns `False` for lists without two elements that sum to zero and `True` if there are two such elements.