
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
    
    lst_len = len(lst)
    if lst_len == 0:
        return 0
    else:
        sum = 0
        for i in range(lst_len):
            if i+1 < lst_len and isinstance(lst[i], int) and lst[i] < 0 and isinstance(lst[i+1], int) and lst[i+1] < 0:
                continue
            elif lst[i] > 0:
                sum += lst[i]**2
        return sum
