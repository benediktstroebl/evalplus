
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if len(lst) == 0:
        return []
    else:
        newList = [min(lst)]
        lst.remove(newList[0])
        if len(lst) == 0:
            return newList
        elif len(lst) == 1:
            return newList + lst
        elif len(lst) == 2:
            return newList + lst
        else:
            newList += [max(lst)]
            lst.remove(max(lst))
            if len(lst) == 1:
                return newList + lst
            elif len(lst) == 2:
                return newList + lst
            else:
                newList += [min(lst)]
                lst.remove(min(lst))
                if len(lst) == 1:
                    return newList + lst
                else:
                    newList += [max(lst)]
                    lst.remove(max(lst))
                    if len(lst) == 1:
                        return newList + lst
                    else:
                        newList += [min(lst)]
                        lst.remove(min(lst))
                        return newList + lst
