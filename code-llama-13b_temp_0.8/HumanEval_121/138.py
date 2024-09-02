
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Make a list with all the values in even positions
    lst_even = []
    for i in range(0, len(lst), 2):
        lst_even.append(lst[i])
    # Make a list with all the odd values
    lst_odd = []
    for i in lst:
        if i % 2 != 0:
            lst_odd.append(i)
    # Sum all the values in lst_odd
    if lst_odd == []:
        return 0
    else:
        return sum(lst_odd)


