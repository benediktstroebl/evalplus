```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension helps checking that if the list has two elements whose sum is equal to zero.

return:
    return any([x + y <= 0 for x, y in zip(l)])

test_cases:
""" 1. 2. 3. - 5. -0
 an example that we do not pass

```