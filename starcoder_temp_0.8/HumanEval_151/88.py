
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
    # List of numbers that are odd.
    odd_numbers = []
    for num in lst:
        # Check if number is positive.
        if num >= 0:
            # Check if number is an integer.
            if num == int(num):
                # Check if number is odd.
                if num % 2!= 0:
                    odd_numbers.append(num)
    # Sum of the squared values of the numbers that are odd.
    return sum([num ** 2 for num in odd_numbers])

