

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # return False

    # # Version 2
    # # O(n^2)
    # # 1795 ms, faster than 25.73% of Python3 online submissions for 3Sum Smaller.
    # # 14 MB, less than 35.14% of Python3 online submissions for 3Sum Smaller.
    # found_sums_to_zero = False
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         for k in range(j+1, len(l)):
    #             if l[i] + l[j] + l[k] == 0:
    #                 found_sums_to_zero = True
    #                 break
    #             else:
    #                 continue
    #     if found_sums_to_zero:
    #         break
    # return found_sums_to_zero

    # Version 3
    # O(n^2)
    # 1354 ms, faster than 68.90% of Python3 online submissions for 3Sum Smaller.
    # 14.3 MB, less than 5.85% of Python3 online submissions for 3Sum Smaller.
    found_sums_to_zero = False
    l = sorted(l)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] + l[j+1] == 0:
                found_sums_to_zero = True
                break
            elif l[i] + l[j] + l[j+1] > 0:
                break
            else:
                continue
        if found_sums_to_zero:
            break
    return found_sums_to_zero


