def triples_sum_to_zero(lst):
    # Using Counter to count occurrences of elements in the list
    cnt = Counter(lst)
    # Filtering elements that can form a sum of zero with another element
    candidates = [k for k, v in cnt.items() if v >= 2 and cnt[k - lst[0]] >= 1 and cnt[k + lst[0]] >= 1]
    return len(candidates) == 3