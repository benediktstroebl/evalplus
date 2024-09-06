def strange_sort_list(lst):
    # Sort the list in a strange way as per the specification
    # Firstly, consider the smallest number and all the other numbers
    # Secondly, consider the largest of the remaining numbers and all the other numbers except the smallest and the largest.
    # Repeat this process until the list is sorted.
    if lst == []:
        return lst
    return strange_sort_list([min(lst)]+[max(lst[:-1])]+min_max(lst[:-2]))
def min_max(lst):
    # This function returns the minimum and maximum of the list at the same time
    return [min(lst), max(lst)]