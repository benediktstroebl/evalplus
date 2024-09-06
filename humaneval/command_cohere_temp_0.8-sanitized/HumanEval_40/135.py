def triples_sum_to_zero(lst):
    # Using Counter to count the number of items with certain values
    cnt = collections.Counter(lst)
    
    # Filtering for the items [x, -x, 0] where x is in the list
    return any(cnt[x] >= 2 and cnt[-x] >= 2 and cnt[0] >= 2 for x in cnt if cnt[x] >= 2 and cnt[-x] >= 2)