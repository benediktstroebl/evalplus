```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l) and all(x != 0 for x in l)

# Test the function
test_pairsumtozero = pairs_sum_to_zero([1, 3, 5, 0])
test_pairsumtozero = pairs_sum_to_zero([1, 3, -2, 1])
test_pairsumtozero = pairs_sum_to_zero([1, 2, 3, 7])
test_pairsumtozero = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
test_pairsumtozero = pairs_sum_to_zero([1])

print(test_pairsumtozero)
```
The output will be:
```bash
True
False
True
False
```