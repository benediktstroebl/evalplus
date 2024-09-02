

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
    # Step 1: Loop through the list
    # Step 2: Square the number
    # Step 3: Round the number to int (Ceiling)
    # Step 4: Add the squared, rounded number to a total variable
    # Step 5: Return total
    
    total = 0
    
    for num in lst:
        num = num**2
        num = math.ceil(num)
        total += num
        
    return total
    
    
    
    
    return result
