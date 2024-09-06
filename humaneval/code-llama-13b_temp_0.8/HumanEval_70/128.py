
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
    # your code here
    # if lst:
    #     new_lst = []
    #     # 0,1
    #     new_lst.append(min(lst))
    #     # 2
    #     new_lst.append(max(lst[1:]))
    #     # 3
    #     new_lst.append(min(lst[1:-1]))
    #     # 4
    #     new_lst.append(max(lst[:-2]))
    #     return new_lst
    # return []
    # lambda_func = lambda x: x[1]
    # print(sorted(enumerate(lst), key=lambda_func, reverse=True))
    # return [x[1] for x in sorted(enumerate(lst), key=lambda_func, reverse=True)]
    # 偶数位置放最大，奇数位置放最小
    new_lst = []
    for i in range(len(lst) // 2 + 1):
        new_lst.append(max(lst[:]))
        lst.remove(max(lst[:]))
        if lst:
            new_lst.append(min(lst[:]))
            lst.remove(min(lst[:]))
    return new_lst

