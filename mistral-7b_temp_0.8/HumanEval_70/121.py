
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

    # 1st idea: iterate through each number and sorting based on conditions.
    # I found this solution to be hard to follow and harder to type so I went
    # with the easier option below.
    #
    # new_lst = []
    # for num in lst:
    #     if len(new_lst) == 0 or num <= new_lst[-1]:
    #         new_lst.append(num)
    #     elif num > new_lst[-1] and num < new_lst[-2]:
    #         new_lst.insert(0, num)
    #
    # return new_lst

    # 2nd idea: Sort list and reverse
    return sorted(lst)[::-1]

