

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Your code here
    even_indicies = []
    odd_indicies = []
    even_list = []
    odd_list = []

    for i in range(len(l)):
        if i % 2 == 0:
            even_indicies.append(i)
        else:
            odd_indicies.append(i)

    for i in even_indicies:
        even_list.append(l[i])

    for i in odd_indicies:
        odd_list.append(l[i])

    even_list.sort()

    new_list = []

    for i in even_indicies:
        new_list.append(even_list[0])
        even_list.remove(even_list[0])

    for i in odd_indicies:
        new_list.append(l[i])

    return new_list
