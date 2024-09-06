
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
    # if the list is empty, return 0
    if not lst:
        return 0
    
    # add up the squares of all odd numbers in the list
    odd_nums = [i for i in lst if i % 2 != 0]
    odd_sum = sum([i**2 for i in odd_nums])
    
    # add the sum of squares of odd numbers to the sum of squares of even numbers
    even_nums = [i for i in lst if i % 2 == 0]
    total_sum = 0
    for i in even_nums:
        total_sum += i**2
    return odd_sum + total_sum
