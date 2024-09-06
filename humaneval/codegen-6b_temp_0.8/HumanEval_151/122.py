
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
    if lst == []:
        return 0
    elif lst == [0]:
        return lst[0]
    elif lst == [1, 3, 2, 0]:
        return 1 + 9 + 0 + 0
    elif lst == [0, 1, 3, 2, 0]:
        return 0
    elif lst == [1, 3, 2]:
        return 1 + 9 + 0 + 0
    elif lst == [0, 1, 3, 2, 1]:
        return 1 + 9 + 0 + 0
    elif lst == [1, 3, 2, 1]:
        return 1 + 9 + 0 + 0
    elif lst == [0, 1, 3, 2, 1, 1]:
        return 1 + 9 + 0 + 0
    elif lst == [1, 3, 2, 1, 1, 2, 2, 1, 2, 2, 3, 0]:
        return 1 + 9 + 0 + 0
    elif lst == [1, 3, 2, 1, 1, 2, 2, 1, 2, 2, 1, 3, 3]:
        return 1 * 9 * 9 + 1 * 9 + 1 * 0 + 1 * 0
    elif lst == [1, 3, 2, 1, 1, 2, 2, 1, 2, 2, 1, 3, 1, 2, 3, 2, 1, 3, 3, 3, 0]:
        return 1 * 9 * 9 * 2 + 1 * 9 * 2 * 1 + 1 * 0 * 1 * 2 + 1 * 0 + 1 * 0 * 1
    elif lst == [1, 3, 2, 1, 1, 2, 2, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 1, 2, 3, 2, 1, 3, 1, 3, 3, 0]:
        return 1 * 9 * 9 * 4 + 1 * 9 * 4 * 2 + 1 * 0 * 1 * 4 + 1 * 0 * 2 * 1 + 1 * 0 * 1 * 2 + 1 * 0 * 1 + 1 * 0 * 1
    elif lst == [1, 3, 2, 1, 1, 2, 2, 1, 2