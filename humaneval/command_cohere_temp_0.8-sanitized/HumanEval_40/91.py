def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sums of pairs of elements in the list
    pairs = Counter(lst)
    # Filtering potential pairs that can sum up to zero
    return any(pairs[x] >= 2 and x + y + z == 0 for x, y in pairs.items() if y < 0)