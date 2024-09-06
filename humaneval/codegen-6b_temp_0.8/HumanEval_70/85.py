
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
        return []

    # put the smallest value at index 0 of new list
    smallest = min(lst) # 1
    smallest_index = lst.index(smallest) # 0
    new_list = [smallest] + lst[:smallest_index]
    # print(new_list)

    # put the largest value at index 1 of new list
    largest = max(lst) # 4
    largest_index = lst.index(largest) # 3
    new_list += lst[largest_index + 1:]
    # print(new_list)

    # put the smallest value at index 2 of new list
    second_smallest = min(lst[:smallest_index] + lst[largest_index+1:]) # 2
    second_smallest_index = lst[:smallest_index] + lst[largest_index+1:].index(second_smallest) # 1
    new_list += [second_smallest] + lst[:second_smallest_index]
    # print(new_list)

    return new_list

