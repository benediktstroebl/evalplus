```python
def triples_sum_to_zero(l):
    if sum(x for x in l if x < 0) <= 2:
        return "Yes"
    else:
        return "No"

# Test the function with provided examples
print(triples_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(triples_sum_to_zero([1, 3, -2, 1]))  # Output: True
print(triples_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))  # Output: True
print(triples_sum_to_zero([1]))           # Output: False
```