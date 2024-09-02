
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

    # check input
    if type(lst) != list:
        print("Not a list")
        return

    # check list is not empty
    if lst == []:
        print("Empty list")
        return

    # check list is not sorted
    if sorted(lst) == lst:
        print("Already sorted")
        return

    # check if list only has one value
    if len(lst) == 1:
        print(lst)
        return

    # make empty list to return
    lst2 = []

    # get smallest and largest in list
    smallest = lst[0]
    largest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

    # add smallest and largest to lst2
    lst2.append(smallest)
    lst2.append(largest)

    # iterate through list of list removing largest and smallest
    for i in lst:
        if i != smallest and i !=
