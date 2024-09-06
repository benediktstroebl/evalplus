def triples_sum_to_zero(lst):
    # Use sorted list to efficiently check if there are three elements that sum to zero
    return not (lst == [] or len(lst) < 3) and any(sum(x) == 0 for i in range(len(lst) - 2) for x in combinations(sorted(lst), 3))