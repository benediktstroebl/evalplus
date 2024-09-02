
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
    new_lst = []
    for x in lst:
        if x < 0 or x % 1!= 0:
            pass
        else:
            if x % 2 == 0:
                new_lst.append(x**2)
            else:
                new_lst.append(x**2)
    return sum(new_lst)
