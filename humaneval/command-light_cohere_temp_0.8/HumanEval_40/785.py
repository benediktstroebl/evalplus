```python
def triples_sum_to_zero(lst):
    if sum(sum(a) for a in lst) == 0:
        return True
    else:
        return False

# Unit tests
test_ triples_sum_to_zero=[1, 3, 5, 0], [1, 3, -2, 1], [1, 2, 3, 7], [2, 4, -5, 3, 9, 7], [1]]
test_ triples_sum_to_zero=None

print(test_ triples_sum_to_zero)
```