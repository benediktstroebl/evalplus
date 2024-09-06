```python
def triples_sum_to_zero(lst):
    # Split the list into pairs and calculate the sum of each pair
    pair_sums = [a + b for a, b in zip(lst, lst[1:])]
    
    # Filter the list of pair sums to get potential triple combinations
    triple_candidates = [sum for sum in pair_sums if sum == 0]
    
    # Filter the original list to get the indices of the potential triple combinations
    candidate_indices = [i for i, x in enumerate(lst) if x in triple_candidates]
    
    # Check if there are exactly three distinct elements
    return len(candidate_indices) == 3

# Tests
assert triples_sum_to_zero([1, 3, 5, 0]) == False
assert triples_sum_to_zero([1, 3, -2, 1]) == True
assert triples_sum_to_zero([1, 2, 3, 7]) == False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1]) == False
```