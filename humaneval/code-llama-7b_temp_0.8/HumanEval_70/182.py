
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
    if lst == []:
        return []
    else:
        temp = lst.copy()
        temp.sort()
        result = []
        temp_list = []
        for i in range(len(temp)):
            for j in range(len(lst)):
                if lst[j] == temp[i]:
                    temp_list.append(lst[j])
            result.append(temp_list[0])
            temp_list = []
        return result
