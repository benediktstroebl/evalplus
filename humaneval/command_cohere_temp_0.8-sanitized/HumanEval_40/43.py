def triples_sum_to_zero(lst):
    # Use sorting to shorten the list and reduce memory usage
    sorted_lst = sorted(lst)
    lst_len = len(sorted_lst)

    # Apply two pointers technique to optimize iteration
    left, right = 0, lst_len - 2

    while left < right:
        if sorted_lst[left] + sorted_lst[right] + sorted_lst[left + 1] == 0:
            return True
        elif sorted_lst[left] + sorted_lst[right] + sorted_lst[left + 1] > 0:
            right -= 1
        else:
            left += 1

    return False