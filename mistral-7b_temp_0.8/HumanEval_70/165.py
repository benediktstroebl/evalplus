
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
    n = len(lst)
    i = 0
    while i < n:
        print(i)
        # print(lst[i])
        for j in range(i+1, n):
            print(j)
            # print(lst[j])
            if lst[i] > lst[j]:
                # print(lst[i])
                # print(lst[j])
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp


        i = i + 1

    print(lst)
    return lst



