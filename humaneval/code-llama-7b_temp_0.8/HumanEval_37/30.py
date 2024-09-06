

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    #create a list for the sorted even values
    sorted_l = []

    #for each even index in l, append the value to the new list
    for i in range(0, len(l), 2):
        sorted_l.append(l[i])

    #sort the list
    sorted_l.sort()

    #use a list comprehension to iterate through the list and return the sorted even values
    #as the value at an even index in the original list
    return [sorted_l[i] if i < len(sorted_l) else None for i in range(len(l))]
