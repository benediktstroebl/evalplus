
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
    if not lst:
        return []
    result = []
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
            elif lst[j] == lst[min_index]:
                if len(result) >= 2:
                    if lst[j] > result[-1] or lst[j] < result[-2]:
                        result.append(lst[j])
                        continue
                    if lst[j] == result[-1]:
                        result.append(lst[j])
                        result.pop()
                        continue
                    if lst[j] == result[-2]:
                        result.pop()
                        continue
                result.append(lst[j])

        result.append(lst[min_index])
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return result


assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
assert strange_sort_list([]) == []

