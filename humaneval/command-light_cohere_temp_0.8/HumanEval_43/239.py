```python
def pairs_sum_to_zero(lst):
    return any(sum(x) == 0 for x in lst)

# Test the function
test_pairsumtozero = lambda: any(pairs_sum_to_zero([1, 3, 5, 0]), 
                                 pairs_sum_to_zero([1, 3, -2, 1]), 
                                 pairs_sum_to_zero([1, 2, 3, 7]), 
                                 pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), 
                                 pairs_sum_to_zero([1]), 
                                 pairs_sum_to_zero([2, 3, 4, 5]))

print(test_pairsumtozero())  # Prints all True
```