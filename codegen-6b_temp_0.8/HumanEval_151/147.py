
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
    # make sure it's a list of numbers
    new_lst = [x for x in lst if not isinstance(x, str) and not isinstance(x, int)]

    if not new_lst:
        return 0

    # make sure the rest of the numbers are even
    for i in new_lst:
        if i % 2 != 0:
            break
    else:
        # if the rest are even, there is nothing to do
        return sum(x**2 for x in new_lst)
    
    # otherwise, we need to apply the Pythagorean Theorem to 
    # eliminate all the even elements.
    new_lst_odd = [x for x in new_lst if x % 2 != 0]
    return sum(new_lst_odd) + sum(x**2 for x in new_lst)
