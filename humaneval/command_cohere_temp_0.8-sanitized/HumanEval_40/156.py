def triples_sum_to_zero(lst):
    # Use Counter to count occurrences of elements in the list
    cnt = Counter(lst)

    # Test if any three distinct elements sum to zero
    for a, b in itertools.combinations(cnt.elements(), 2):
        if not cnt[a] and not cnt[b] and a + b + cnt[abs(a - b)] == 0:
            return True
    return False