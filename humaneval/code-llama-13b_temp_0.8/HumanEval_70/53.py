
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

    # size = len(lst)
    # if size <= 1:
    #     return lst

    # temp = lst.copy()
    # temp.sort()
    # result = [temp[0]]
    # for i in range(1, size):
    #     if i % 2 == 1:
    #         result.append(temp[-i])
    #     else:
    #         result.append(temp[i])

    # return result
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return lst[0:n:2] + lst[1:n:2]
    else:
        return lst[0:n:2] + lst[2:n:2] + lst[1:n:2]

