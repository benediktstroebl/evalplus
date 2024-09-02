

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # 1. for every even index, find the min of l[indx:end]
    # 2. swap l[indx] with the min
    # 3. reverse the remaining list
    # 4. concatenate the min value to the first half of the list

    l = list(l)  # dont want to alter the original list.
    evens = [l[i] for i in range(0, len(l), 2)]
    odds = [l[i] for i in range(1, len(l), 2)]

    odds.sort()
    for i in range(len(evens)):
        evens[i], odds[i] = odds[i], evens[i]

    # return sorted(l)
    return evens + odds

