
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
    # validate input and return 0 if input is invalid
    if not isinstance(lst, list) or len(lst) == 0 or (isinstance(lst[0], int) and lst[0] == 0):
        return 0
    
    # check if numbers in list are non-negative integers and if so, add them to a new list
    numbers_lst = [number for number in lst if number > 0 and isinstance(number, int)]
    # add the square of each odd number in the new list to a new list
    squared_numbers_lst = [number ** 2 for number in numbers_lst if number % 2 != 0]
    # return the sum of the new list
    return sum(squared_numbers_lst)

