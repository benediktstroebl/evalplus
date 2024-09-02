

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    if len(l) < 3:
        return l

    result = []

    for i in range(0, len(l), 3):
        if i == 0:
            first = l[i]
            second = l[i+1]
            third = l[i+2]
            if first < second:
                if second < third:
                    result.append(first)
                    result.append(second)
                    result.append(third)
                else:
                    result.append(first)
                    result.append(third)
                    result.append(second)
            else:
                if first < third:
                    result.append(third)
                    result.append(first)
                    result.append(second)
                else:
                    result.append(second)
                    result.append(first)
                    result.append(third)
        else:
            if l[i-1] < l[i+1]:
                result.append(l[i])
            else:
                result.append(l[i-2])
                result.append(l[i-1])
                result.append(l[i])

    return result

