def triples_sum_to_zero(lst):
    # Use counter to quickly find distinct elements with nonzero counts
    # Then find three elements with counts that multiply to zero
    counts = Counter(lst)
    for x in counts:
        if counts[x] > 2 and counts[x] * (counts[x] - 1) * (counts[x] - 2) == 0:
            return True
    return False