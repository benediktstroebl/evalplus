

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Sorted list is used to make it constant-time
    # instead of linear search
    sorted_list = sorted(l)
    cnt = 0
    for i in range(len(sorted_list)):
        cnt += 1
        if cnt > 1:
            return True
        if i > 0 and sorted_list[i] == sorted_list[i-1]:
            continue
        complement = sorted_list[i]
        lo, hi = i+1, len(sorted_list) - 1
        while lo < hi:
            if sorted_list[lo] + sorted_list[hi] == complement:
                return True
            elif sorted_list[lo] + sorted_list[hi] < complement:
                lo += 1
            else:
                hi -= 1
    return False
        
