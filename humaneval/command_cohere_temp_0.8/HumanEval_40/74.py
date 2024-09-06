```python
def triples_sum_to_zero(lst):
    # Using Counter to count the number of items with certain values
    cnt = collections.Counter(lst)
    
    # Filtering for the items [x, -x, 0] where x is in the list
    return any(cnt[x] >= 2 and cnt[-x] >= 2 and cnt[0] >= 2 for x in cnt if cnt[x] >= 2 and cnt[-x] >= 2)
```

The solution uses `collections.Counter` to count the number of items with certain values. Then it checks if there are any items `x` such that both `cnt[x]` and `cnt[-x]` are at least 2, as well as `cnt[0]` (assuming that `0` is among the values). If there are any such items, it returns `True`. The condition for `any` is that there exist three distinct elements that sum up to zero. The order of the items doesn't matter, as long as all three items are present in the list.