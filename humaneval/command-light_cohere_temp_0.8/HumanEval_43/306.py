Here is a Python script that contains a self-contained function to solve the problem:
```python
def pairs_sum_to_zero(l):
    """
    checks if there are two distinct elements in the list that sum to zero, 
    and returns a boolean value accordingly.
    """
    list comprehension is filtered elements are those whose elements in a pair 
    add up to zero.
    """
    pairwise numbers that add up to zero."""
    return sum(x+y for x,y in zip(l)) <= 0

test_cases = [
    [ [1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 5, 7], [1]]
]

for test in test_cases:
    print(pairs_sum_to_zero(test))
```
The `pairs_sum_to_zero` function uses a list comprehension and the `sum()` function to determine if there are two elements in the list that sum to zero. The function returns `True` if the list contains two elements that sum to zero, and `False` otherwise.