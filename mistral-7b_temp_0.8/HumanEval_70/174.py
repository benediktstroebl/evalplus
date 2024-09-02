
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
    # Your code here
    #todo: implement
    # Don't forget to return the result!
    #lst = [1, 2, 3, 4]
    #print(lst)
    lst.sort()
    lst.reverse()
    #print(lst)
    return lst
