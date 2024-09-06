def triples_sum_to_zero(lst):
    # Using Counter to count occurrences of elements in the list
    cnt = Counter(lst)
    
    # Check if any (a, b, -a-b) is present in the list
    return (-cnt[a] - cnt[b] > 0 for a in cnt for b in cnt if a != b)