
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
    # IMPLEMENT THIS METHOD
    if len(lst) == 0:
        return 0
    double_lst = []
    for each in lst:
        if each < 0 or not type(each) == int:
            continue
        else:
            double_lst.append(each*each)
    sum_of_squares = 0
    for each in double_lst:
        if each % 2 == 1:
            sum_of_squares += each
    return sum_of_squares
    
            

    
