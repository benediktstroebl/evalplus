
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
    def get_min_max(lst):
        '''Return min and max from list'''
        return [min(lst), max(lst)]

    def get_odd_even(lst):
        '''
        Return odd and even from list.
        '''
        odd = []
        even = []
        for i in lst:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return [odd, even]

    def get_reverse(lst):
        '''Return reversed list'''
        return lst[::-1]

    def reverse_sort(lst):
        '''
        Return sorted list in reverse order.
        '''
        lst_min_max = get_min_max(lst)
        lst_odd, lst_even = get_odd_even(lst)
        lst = lst_min_max + lst_odd + lst_even
        lst = get_reverse(lst)
        return lst

    return reverse_sort(lst)
