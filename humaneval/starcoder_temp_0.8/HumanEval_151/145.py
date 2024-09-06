
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
    # Your code here
    
    if lst == []:
        return 0
    else:
        new_lst = []
        for item in lst:
            if type(item) == int and item >= 0:
                new_lst.append(item)
            else:
                pass
        if new_lst == []:
            return 0
        else:
            result = 0
            for item in new_lst:
                result = result + item**2
            result = result - sum(new_lst)
            return result
    
