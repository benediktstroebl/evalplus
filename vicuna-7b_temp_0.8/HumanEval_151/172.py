
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
    if not lst:
        return 0
    
    # Find the sum of the list
    lsum = sum(lst)
    
    # Find the number of odd numbers in the list
    odd_nums = [i for i in lst if i % 2 != 0]
    num_odd = len(odd_nums)
    
    # Return the sum of the squares of the odd numbers
    return (num_odd * (num_odd - 1) // 2) + lsum ** 2
