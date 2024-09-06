
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
    def merge_pairs(lst):
        result = []
        while lst:
            if lst[-1] < lst[-2]:
                result.append(lst.pop())
            else:
                result.append(lst.pop())
            lst.pop()
        return result

    min_val = lst[0]
    max_val = lst[-1]

    for i in range(1, len(lst)):
        if lst[i] >= max_val:
            merge_pairs(lst[:i] + [lst[i]])
        else:
            merge_pairs(lst[:i])

    return merge_pairs(lst)

lst = [2, 3, 1, 5, 4, 5, 5, 5, 5]
print(strange_sort_list(lst))
