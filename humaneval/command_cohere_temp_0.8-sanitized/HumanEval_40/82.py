def triples_sum_to_zero(lst):
    # Sort the list in order to make the detection of three distinct elements with sum zero easier
    lst = sorted(lst)
    return any(x + y + z == 0 for x in lst for y in lst[1:] for z in lst[1:])