```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Test the function
test_pairsumtozero = lambda: any(pairsumtozero([1, 3, 5, 0]), pairsumtozero([1, 3, -2, 1]), pairsumtozero([1, 2, 3, 7]), pairsumtozero([2, 4, -5, 3, 5, 7]))

print(test_pairsumtozero())
```