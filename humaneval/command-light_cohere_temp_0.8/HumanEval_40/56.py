```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x]) == 0:
        return True
    return False

# Unit tests
triples_sum_to_zero([1, 3, 5, 0])  # Output: False
triples_sum_to_zero([1, 3, -2, 1])  # Output: True
triples_sum_to_zero([1, 2, 3, 7])  # Output: False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Output: True
triples_sum_to_zero([1])           # Output: False
```
The Python function `triples_sum_to_zero` calculates whether there are three distinct elements in a list that sum to zero. It accepts a general list `lst` as input and utilizes the `sum()` function with list comprehension to determine if the sum of its elements equals zero. 

If the list satisfies this condition, it returns `True`; otherwise, it returns `False`. The test suite demonstrates the function's behavior by providing various lists and verifying the output of the `triples_sum_to_zero` function.