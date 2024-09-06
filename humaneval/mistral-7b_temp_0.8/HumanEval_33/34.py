

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = list(l)
    l2 = [0] * len(l)
    #print(f'l2: {l2}')
    for i in range(len(l)):
        if i%3==0:
            l2[i]=sorted(l[i:i+3])[2]
            #print(f'l2[{i}]: {l2[i]}')
        else:
            l2[i]=l[i]
    return l2
