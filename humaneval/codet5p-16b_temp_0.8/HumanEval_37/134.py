

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    
    l_copy = l[::]
    even_indicies = []
    for i in range(len(l_copy)):
        if i % 2 == 0:
            even_indicies.append(i)
    for i in range(len(even_indicies)):
        l_copy[even_indicies[i]] = l_copy[even_indicies[i]][::]
        for j in range(len(l_copy[even_indicies[i]])):
            l_copy[even_indicies[i]][j] = l_copy[even_indicies[i]][j][::]
            for k in range(len(l_copy[even_indicies[i]][j])):
                l_copy[even_indicies[i]][j][k] = l_copy[even_indicies[i]][j][k][::]
                l_copy[even_indicies[i]][j][k][0] = l_copy[even_indicies[i
