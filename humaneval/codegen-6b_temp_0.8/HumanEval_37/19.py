

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    
    # Use a for loop, if one for statement, the other if statement will be
    # executed first and the first for loop will not be executed. In other
    # words, if first for statement is not executed, the second for statement
    # will be executed.
    
    # l2 = [l[i] for i in range(len(l)) if i%2==1] # This is inefficient, as the for loop repeats over the entire list, and the length is very high
    # for i in range(len(l) - 1):
    #     if l[i] > l[i + 1]:
    #         l[i], l[i + 1] = l[i + 1], l[i]
    # return l2

    # This is quicker, as the list is only sent back, and not returned. Can also use the lambda function.
    return sorted(l, key = lambda x: (x%2, x))
