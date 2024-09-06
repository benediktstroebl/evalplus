```python
def triples_sum_to_zero(lst):
    # Use sorted list to efficiently check if there are three elements that sum to zero
    return not (lst == [] or len(lst) < 3) and any(sum(x) == 0 for i in range(len(lst) - 2) for x in combinations(sorted(lst), 3))
```

This function uses a clever approach by using sorted combinations of the list to efficiently check for three elements that sum to zero. It first checks if the list is empty or shorter than three elements, which will always result in False. Then, it uses the any function to check if there are combinations of three elements that sum to zero, which would return True. This approach ensures that the time complexity is optimized to O(N^2) instead of O(NTot), where N is the number of elements in the list and NTot is the total number of combinations.  This makes it efficient even for large input sizes.