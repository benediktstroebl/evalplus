def triples_sum_to_zero(lst):
    # Sort the list in non-decreasing order - this allows us to eliminate possibilities
    # for the first and second element in the potential triple that sums to zero.
    sorted_lst = sorted(lst)
    for i in range(len(sorted_lst) - 2):
        if sorted_lst[i] + sorted_lst[i+1] == 0:
            return True
    return False