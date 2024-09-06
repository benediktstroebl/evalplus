
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
    # Convert the list to an array of integers
    arr = list(map(int, lst))
    
    # Initialize a variable to store the sum of squares of odd numbers
    odd_sum = 0
    
    # Iterate through the array
    for i in range(len(arr)):
        # If the number is odd and positive or non-negative, add its square to the sum
        if (arr[i] > 0) or (arr[i] >= 0):
            odd_sum += arr[i]**2
            
    # Return the sum of squares of odd numbers
    return odd_sum