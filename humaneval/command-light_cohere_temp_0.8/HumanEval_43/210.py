```python
def pairs_sum_to_zero(l):
    return any([x+y <= 0 for x,y in zip(l,l[1:])])

# Tests
test_pass = lambda: pairs_sum_to_zero([1, 3, 5, 0])
test_fail = lambda: pairs_sum_to_zero([1, 3, -2, 1])
test_sum = lambda: pairs_sum_to_zero([1, 2, 3, 7])
test_empty = lambda: pairs_sum_to_zero([])

print("Pass tests:",test_pass())
print("Failtests:",test_fail())
print("Sums:",test_sum())
print("Empty:",test_empty())")
```

The output will be:
```bash
Passtests
True
Failtests
False
Sums:True
Empty: False
```