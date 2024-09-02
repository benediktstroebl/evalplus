
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

    # Step 1: sort list in ascending order
    # Step 2: set variable to 1
    # Step 3: iterate through sorted list
    # Step 4: if list index is even, return min, else return max
    # Step 5: if list index is odd, return max, else return min
    # Step 6: pass all to function

    def min_max(lst):
        sorted_lst = sorted(lst)
        i = 0
        new_lst = []
        while i < len(sorted_lst):
            if i % 2 == 0:
                new_lst.append(min(sorted_lst[i:]))
            else:
                new_lst.append(max(sorted_lst[i:]))
            i += 1
        return new_lst

    return min_max(lst)

