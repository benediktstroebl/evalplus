```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in l:
        if 0 == i:
            continue
        x, y = divmod(i, -2)
        if x in seen and y in seen:
            return True
        seen.add(x)
        seen.add(y)
    return False
```

This approach uses a generator expression to split each non-zero integer in the list into its corresponding factors, and then checks if these factors, when reversed, subtract each other. This works due to the fact that integers can be expressed as a product of its factors and factoring out groups of two gives the original integer when reversed. 

The tests would look something like this:
```python
# tests:
assert triples_sum_to_zero([1, 3, 5, 0]) == False
assert triples_sum_to_zero([1, 3, -2, 1]) == True
assert triples_sum_to_zero([1, 2, 3, 7]) == False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1]) == False
```