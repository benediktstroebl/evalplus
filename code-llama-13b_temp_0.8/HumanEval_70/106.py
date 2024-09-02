
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
    # 1. Create a local variable to store the index of the element
    # that will be taken from the list
    # 2. Create an empty list to store the result
    # 3. Take the first element
    # 4. Loop while there are elements in the list
    # 5. Inside the loop create a local variable that will be the
    # sorted list
    # 6. Sort the list by the selected element
    # 7. Take the selected element from the list
    # 8. Add the selected element to the result list
    # 9. Return the result list

    # Solution with enumerate
    # result = []
    # idx = 0
    # while lst:
    #     sorted_lst = sorted(lst, key=lambda x: x[idx])
    #     result.append(sorted_lst.pop(0))
    # return result

    # Solution without enumerate
    result = []
    while lst:
        idx = 0 if len(lst) % 2 else 1
        sorted_lst = sorted(lst, key=lambda x: x[idx])
        result.append(sorted_lst.pop(idx))
    return result

