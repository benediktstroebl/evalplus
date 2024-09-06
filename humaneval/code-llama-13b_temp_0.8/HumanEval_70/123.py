
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
        return lst
    # your code here
    def find_max(arr):
        max_val = arr[0]
        for val in arr:
            if val > max_val:
                max_val = val
        return max_val

    def find_min(arr):
        min_val = arr[0]
        for val in arr:
            if val < min_val:
                min_val = val
        return min_val
    # print(lst)
    sorted_list = [find_min(lst)]
    while len(lst) > 0:
        lst.remove(find_min(lst))
        lst.remove(find_max(lst))
        sorted_list.append(find_min(lst))
    return sorted_list

