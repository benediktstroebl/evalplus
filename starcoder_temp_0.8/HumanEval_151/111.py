
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
    else:
        lst_2 = [i for i in lst if type(i) == int and i > 0]
        squares = [i ** 2 for i in lst_2 if i % 2!= 0]
        return sum(squares)
