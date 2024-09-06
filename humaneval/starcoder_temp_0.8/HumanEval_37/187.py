

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_list = l[:]
    even_nums = []
    odd_nums = []
    for i in range(0, len(l)):
        if i % 2 == 0:
            even_nums.append(l[i])
        else:
            odd_nums.append(l[i])
    even_nums.sort()
    for i in range(0, len(l)):
        if i % 2 == 0:
            new_list[i] = even_nums[i//2]
    for i in range(1, len(l)):
        if i % 2!= 0:
            new_list[i] = odd_nums[i//2]
    return new_list
