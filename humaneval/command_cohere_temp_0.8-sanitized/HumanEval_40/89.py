def triples_sum_to_zero(lst):
    # Use sorted() to allow for multiple trips sum to zero
    return next((True for x, y, z in sorted(zip(lst, lst[1:], lst[2:])) if x + y + z == 0), False)