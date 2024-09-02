

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # The following implementation is based on a merge sort algorithm
    # on a list of tuples (even, odd)
    if len(l) % 2 == 0:
        l = [x for x in zip(l[::2], l[1::2])]
        def merge(l1, l2):
            i1 = 0
            i2 = 0
            result = []
            while i1 < len(l1) and i2 < len(l2):
                if l1[i1][0] <= l2[i2][0]:
                    result.append(l1[i1])
                    i1 += 1
                else:
                    result.append(l2[i2])
                    i2 += 1
            result.extend(l1[i1:])
            result.extend(l2[i2:])
            return result
        def merge_sort(l):
            if len(l) == 1:
                return l
            else:
                half_len = len(l)//2
                l1 = merge_sort(l[:half_len])
                l2 = merge_sort(l[half_len:])
                return merge(l1, l2)
        l = merge_sort(l)
        return [x for t in l for x in t]
    else:
        return l

