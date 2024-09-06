```python
def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sums of pairs of elements in the list
    pairs = Counter(lst)
    # Filtering potential pairs that can sum up to zero
    return any(pairs[x] >= 2 and x + y + z == 0 for x, y in pairs.items() if y < 0)
```

The function relies on the property that in a list of distinct elements, if there are three elements that sum to zero, at least one of those elements must have a negative counterpart. The code utilizes Python's `Counter` to efficiently find these elements that sum to zero. It checks if there are at least two occurrences of an element that has a negative counterpart, and if so, it returns `True`. The `any` usage iterates through the keys and values of the Counter object to find suitable triples. 

This solution has an time complexity of O(n log n), where n is the length of the input list, which arises from the necessity to use two loops in the any function.