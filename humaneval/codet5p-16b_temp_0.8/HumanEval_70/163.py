
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

    result = []
    numbers = [str(i) for i in lst]
    for num in numbers:
        min_num = min(num, numbers)
        max_num = max(num, numbers)
        result.append(max_num)
        result.append(min_num)
        numbers.remove(max_num)
    return [int(i) for i in result]
