
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

    def chunk(a, b):
        while len(a) > 0:
            yield a[:b]
            a = a[b:]

    assert isinstance(lst, list)

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return lst

    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return lst

    # Find the minimum value
    mn = min(lst)
    # Find the maximum value
    mx = max(lst)
    # Find the length of the list
    l = len(lst)

    # The indices of the minimum, maximum, and first numbers in the list
    mn_idx = lst.index(mn)
    mx_idx = lst.index(mx)
    first_idx = 0

    # Check if the first element is the minimum value
    if lst[0] == mn:
        # If it is the case, swap the first two elements
        lst[0], lst[1] = lst[1], lst[0]
        # Set the first index to 1
        first_idx = 1

    # Set the numbers we will be using
    # First number is lst[first_idx]
    # Last number is lst[last_idx]
    # Minimum number is lst[mn_idx]
    # Maximum number is lst[mx_idx]
    last_idx = l - 1

    # Set the order of the numbers we are going to use
    order = [first_idx, last_idx, mn_idx, mx_idx]

    # Chunk the list into four parts
    a, b, c, d = chunk(lst, 1)

    # Reorder the numbers
    a = a[order[0]]
    b = b[order[1]]
    c = c[order[2]]
    d = d[order[3]]

    # Return the joined list
    return a + b + c + d

