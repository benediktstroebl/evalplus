
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
    # make a list of odd numbers
    odd_lst = [i for i in lst if i%2 != 0 and i >= 0]
    # square odd numbers
    square_lst = [i**2 for i in odd_lst]
    # return the sum
    return sum(square_lst)
