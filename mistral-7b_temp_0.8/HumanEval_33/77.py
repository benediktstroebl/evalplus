

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # TODO:
    # Think of the case when there are no indicies divisible by three.
    #
    # What happens to your solution in that case?
    #
    # Can you make it so that this problem never happens?
    #
    # How?
    #
    # Hint: When you iterate through the list, what happens when you
    # encounter an index that is divisible by three?
    #
    # Remember: you can remove elements from the list by using list.pop().

    result = []
    i = 0
    while i < len(l):
        if i % 3 != 0:
            result.append(l[i])
            i += 1
        else:
            l.pop(i)
            result.append(sorted(l[i::3])[0])
            i += 1

    return result

