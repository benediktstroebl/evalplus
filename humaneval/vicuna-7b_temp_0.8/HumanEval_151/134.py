
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
    lst = list(map(int, lst))  # convert the list to a list of integers
    even_lst = filter(lambda x: x % 2 == 0, lst)  # get even numbers
    odd_lst = filter(lambda x: x % 2 != 0, lst)  # get odd numbers
    return sum([x**2 for x in odd_lst if x > 0])