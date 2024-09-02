

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # Code from Chapter 4, Doctesting
    # l2 = [3*i for i in range(len(l)/3)]
    # l3 = l[:len(l)/3]
    # l4 = [3*i for i in range(len(l)/3, 2*len(l)/3)]
    # l5 = l[len(l)/3:2*len(l)/3]
    # l6 = [3*i for i in range(2*len(l)/3, len(l))]
    # l7 = l[2*len(l)/3:len(l)]

    # return l3 + sorted(l2) + l4 + sorted(l5) + l6 + sorted(l7)

    # Code from Chapter 4, Doctesting
    # return (l[:len(l)/3] + sorted(l[len(l)/3:2*len(l)/3]) + l[2*len(l)/3:])

    # My code
    # try:
    #     third = len(l)/3
    #     return l[:third] + sorted(l[third:2*third]) + l[2*third:]
    # except TypeError:
    #     return l

    # My code
    try:
        third = len(l)/3
        return l[:third] + sorted(l[third:2*third]) + l[2*third:]
    except TypeError:
        return l

































































































































































