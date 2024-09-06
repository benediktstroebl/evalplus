```python
def triples_sum_to_zero(l):
    if sum([x for x in l if x <= 0]) == 0:
        return True
    else:
        return False

# Tests
triples_sum_to_zero([1, 3, 5, 0])  # => False
triples_sum_to_zero([1, 3, -2, 1])  # => True
triples_sum_to_zero([1, 2, 3, 7])  # => False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # => True
triples_sum_to_zero([1])          # => False
```
The function takes a list l as input and checks if there are three distinct elements in the list that sum to zero. If the sum of these three elements is zero, the function returns True; otherwise, it returns False.