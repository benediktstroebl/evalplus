def triples_sum_to_zero(lst):
    # Define possible pairs with differences summing to zero
    pairs = [(x, lst[idx + 1] - x) for idx, x in enumerate(lst) if x != lst[idx + 1]]
    return len(pairs) == 3 and all(sum(p) == 0 for p in pairs)