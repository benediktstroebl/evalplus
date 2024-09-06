def triples_sum_to_zero(lst):
    # Using Counter to quickly find potential triple combinations that sum to zero
    combinations = collections.Counter(zip(lst, lst[1:], lst[2:]))
    return combinations.get((-1, 0, 1)) is not None