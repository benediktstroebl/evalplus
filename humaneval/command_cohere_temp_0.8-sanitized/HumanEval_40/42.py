def triples_sum_to_zero(lst):
    # Use sorting to cluster elements with the same value
    sorted_lst = sorted(lst)
    grouped_lst = [list(group) for group in itertools.groupby(sorted_lst)]

    for a, b, _ in combinations(grouped_lst, 3):
        if a[0] + b[0] == 0:
            return True

    return False