

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l_new = [0] * (len(l)*2)
    for i in range(0, len(l)):
        if i % 2 == 1:
            l_new[i] = l[i//2]
        else:
            l_new[i] = l[i//2]
            j = i//2
            while j >= 0:
                if l[j] > l[j+1]:
                    l_new[i], l_new[j] = l_new[j], l_new[i]
                    i = j
                else:
                    j -= 1
    return l_new
