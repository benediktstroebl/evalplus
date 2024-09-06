```python
def pairs_sum_to_zero(l):
    # iterate through all pairs
    for x, y in combinations(l, 2):
        if x + y == 0:
            return True
    return False
```

This function uses a combination iterator to check if any pairs in the list sum up to zero. The iterator creates all possible pairs of elements from the list, and the function adds up the elements of each pair and checks if the sum is equal to zero. If it is, the function returns True, if not, it returns False. 

Such a solution strongly utilizes Python's built-in capabilities to handle pairs and sums in an elegant and efficient way. 

This solution has a time complexity of O(n^2), as it checks all possible pairs, which is necessary to ensure we catch all pairs that sum up to zero. 

If the list is very large, this approach may become computationally expensive. However, for small lists or those with a small number of distinct elements, it is efficient enough and simple to understand and maintain.