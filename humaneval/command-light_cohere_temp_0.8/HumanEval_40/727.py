```python
def triples_sum_to_zero(lst):
    """
    Checks whether there are three distinct elements in lst that sum to zero.
    Returns: True if they can be represented as three integers, and False otherwise.
    """
    sum(a * b * c for a,b,c in zip(lst, lst, lst)) == 0

# Test the function:
lst = [1, 3, 5, 0]
result = triples_sum_to_zero(lst)
print(result)

lst = [1, 3, -2, 1]
result = triples_sum_to_zero(lst)
print(result)

lst = [1, 2, 3, 7]
result = triples_sum_to_zero(lst)
print(result)

lst = [2, 4, -5, 3, 9, 7]
result = triples_sum_to_zero(lst)
print(result)
```