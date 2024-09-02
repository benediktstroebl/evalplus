
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    def num_sort(nums):
        return sorted(nums, key=abs)
    lst_num = [abs(n) for n in lst if isinstance(n, int)]
    if len(lst_num) == 0:
        return (None, None)
    return (num_sort(lst_num)[0], num_sort(lst_num)[-1])
