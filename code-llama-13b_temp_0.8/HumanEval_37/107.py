

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indicies = [i for i in range(len(l)) if i % 2 == 0]
    odd_indicies = [i for i in range(len(l)) if i % 2 == 1]
    even_elements = [l[i] for i in even_indicies]
    odd_elements = [l[i] for i in odd_indicies]
    sorted_even = sorted(even_elements)
    combined = []
    for i in range(len(l)):
        if i in even_indicies:
            combined.append(sorted_even.pop(0))
        elif i in odd_indicies:
            combined.append(odd_elements.pop(0))
    return combined

