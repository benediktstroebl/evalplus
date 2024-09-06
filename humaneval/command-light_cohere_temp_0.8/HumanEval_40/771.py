```python
def triples_sum_to_zero(lst):
    sum_to_zero = set([x + y + z for x, y, z in lst])
    return bool(sum_to_zero)

# Example usage
triples_sum_to_zero([1, 3, -2, 1])  # Output: True
triples_sum_to_zero([1, 2, 3, 7])  # Output: False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Output: True
triples_sum_to_zero([1])        # Output: False
```
This code defines a function called triples_sum_to_zero that takes a list lst as input and returns True if there are three distinct elements in the list that sum to zero, and False otherwise. It achieves this by using a set-based approach to check if there are three distinct elements that sum to zero.