
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
    # Your code goes here
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append(lst[0])
            for j in range(len(lst)-1):
                if lst[j] > lst[j+1]:
                    result.append(lst[j+1])
                    break
        else:
            if lst[i] > lst[i-1]:
                result.append(lst[i])
            else:
                result.append(lst[i-1])
    return result
