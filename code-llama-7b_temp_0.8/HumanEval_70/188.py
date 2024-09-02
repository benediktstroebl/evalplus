
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

    # Base case: empty list
    if lst == []:
        return lst

    # Initialize variables
    i = 0
    n = len(lst)
    s_lst = []

    # Use two loops to extract min and max
    for i in range(n):
        # Smallest element
        small = lst[0]

        # Max element
        max_ = lst[0]

        # Loop through the list to find min, max
        for j in range(n):
            # Find smallest
            if lst[j] < small:
                small = lst[j]

            # Find max
            if lst[j] > max_:
                max_ = lst[j]

        # Append the min into a separate list
        s_lst.append(small)

        # Append the max into a separate list
        s_lst.append(max_)

    # print(s_lst)
    return s_lst
