def triples_sum_to_zero(lst):
    # Sort the list in non-decreasing order
    sorted_lst = sorted(lst)
    # Use a hashset to keep track of elements encountered during iteration
    encountered = set()
    for i in range(len(sorted_lst) - 2):
        a = sorted_lst[i]
        for j in range(i + 1, len(sorted_lst) - 1):
            b = sorted_lst[j]
            if a + b == sorted_lst[j + 1] and (a, b) not in encountered:
                encountered.add((a, b))
                if i + 1 < j and (b, a) not in encountered:
                    return True
    return False