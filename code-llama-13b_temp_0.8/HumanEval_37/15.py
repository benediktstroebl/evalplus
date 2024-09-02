

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # lst = l[:]
    # i = 0
    # while i < len(l):
    #     if i % 2 == 0:
    #         j = i
    #         while j < len(l):
    #             if l[j] < l[i]:
    #                 j += 2
    #             else:
    #                 temp = l[i]
    #                 l[i] = l[j]
    #                 l[j] = temp
    #                 j += 2
    #     i += 2
    # return lst
    return sorted(l, key=lambda x: x % 2)
