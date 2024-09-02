

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    # Given list
    lst = [1,2,3]
    
    # Initalize the sum value
    sum = 0
    
    # Loop through the list
    for i in lst:
        
        # Round the elements in the list up to the nearest integer
        i = int(math.ceil(i))
        
        # Square each element in the list
        i = i ** 2
        
        # Add each element to the sum
        sum = sum + i
    
    # Print the sum
    print(sum)
