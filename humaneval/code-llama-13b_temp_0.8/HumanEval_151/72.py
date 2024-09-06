
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
    
    # This function is called recursively. It takes the list and the sum of the squares of the odd numbers in it.
    # It then goes through the list until it finds the first element which is an odd number.
    # Then, it calls the function again to find the sum of the squares of the odd numbers in the remaining list.
    # If the list is empty, it returns the sum.
    # Otherwise, it adds the sum of the squares of the odd numbers in the list, to the square of the odd number that it found and then returns it.
    # If the element is not an odd number, the function just returns the sum of the squares of the odd numbers in the list that it found.
    # If there are no odd numbers in the list, it returns 0.
    
    def get_sum(lst, sum_of_squares):
        if not lst:
            return sum_of_squares
        if lst[0] % 2 != 0 and lst[0] >= 0:
            sum_of_squares += lst[0] ** 2
        return get_sum(lst[1:], sum_of_squares)
    
    return get_sum(lst, 0)
