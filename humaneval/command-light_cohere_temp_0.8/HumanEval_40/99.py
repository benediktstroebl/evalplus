```python
def triples_sum_to_zero(lst):
    return any(sum(x) == 0 for x in lst) and all(x != 0 for x in lst)

test_ triples_sum_to_zero=[1, 3, 5, 0]
test_ triples_sum_to_zero=[1, 3, -2, 1]
test_ triples_sum_to_zero=[1, 2, 3, 7]
test_ triples_sum_to_zero=[2, 4, -5, 3, 9, 7]
test_ triples_sum_to_zero=[1]
test_ triples_sum_to_zero=[]

# Output:
```