
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
    def reverse(lst):
        return lst[::-1]

    def strange_sort(lst):
        n = len(lst)
        if n == 0:
            return []
        elif n == 1:
            return [lst[0]]
        else:
            result = []
            for i in range(1, n):
                reversed_lst = reverse(lst[:i])
                result.append(lst[i])
                result.extend(reversed_lst)
            return result

    return strange_sort(lst)
