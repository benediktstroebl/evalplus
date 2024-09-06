
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
    # Find the largest integer
    largest = max(lst)
    # Find the minimum of the remaining integers
    min_remaining = min(lst[1:])
    # If the largest integer is odd, reverse the largest integer and the remaining
    # integers, so that the largest integer becomes the first element
    if largest % 2 == 1:
        lst.insert(0, largest)
        lst.insert(0, min_remaining)
    else:
        lst.insert(0, largest)
        lst.insert(0, min_remaining)
        # Find the remaining integers
        remaining = [lst.pop(0)]
        # Add the largest integer to the remaining integers
        remaining.append(largest)
        # Append the remaining integers
        lst.extend(remaining)
    return lst