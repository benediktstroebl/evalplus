
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    # List is empty
    if lst == []:
        return 0
    # List contains only negative numbers
    elif len(lst) == 1 and lst[0] < 0:
        return 0
    # List contains only zeros
    elif len(lst) == 1 and lst[0] == 0:
        return 0
    # List contains only positive numbers
    elif len(lst) == 1 and lst[0] > 0:
        return lst[0] ** 2
    # List contains only negative numbers
    elif len(lst) == 1 and lst[0] < 0:
        return 0
    # List contains a mix of positive and negative numbers
    elif len(lst) > 1 and lst[0] > 0 and lst[1] < 0:
        return (lst[0] ** 2) + (lst[1] ** 2)
    # List contains only positive numbers
    elif len(lst) > 1 and lst[0] > 0:
        return (lst[0] **
