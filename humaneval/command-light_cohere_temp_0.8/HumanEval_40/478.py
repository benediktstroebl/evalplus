```python
def triples_sum_to_zero(lst):
    if sum(map(int, lst)) < 0:
        return True
    return False

# Test the function with known solutions
print(triples_sum_to_zero([1, 3, -2, 1])))  # True
print(triples_sum_to_zero([1, 2, 3, 7])))    # False
print(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))) # True
print(triples_sum_to_zero([1]))           # False
```