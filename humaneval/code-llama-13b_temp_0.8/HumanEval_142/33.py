


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    # Need to iterate over the list.
    
    # Check if index is a multiple of 3
    # If the index is a multiple of 3, square the integer.
    # Check if index is a multiple of 4
    # If the index is a multiple of 4, cube the integer.
    # Else, add the integer to a running total.
    
    # You can use the modulus operator to see if a number is evenly divisible by something.
    # E.g. if you want to check if something is divisible by three:
    # if num % 3 == 0:
    # ...
    # Here is a list of modulus operations to check divisibility:
    # 5 % 2 = 1 (not divisible)
    # 5 % 3 = 2 (divisible)
    # 5 % 4 = 1 (not divisible)
    # 5 % 5 = 0 (divisible)
    # 5 % 6 = 5 (not divisible)
    
    # Initialize a running total
    total = 0
    
    # Iterate over the list
    for i in range(len(lst)):
        
        # Check if the index is a multiple of 3
        # If so, square the number
        if i % 3 == 0:
            lst[i] = lst[i]**2
            
        # Check if the index is a multiple of 4
        # If so, cube the number
        if i % 4 == 0:
            lst[i] = lst[i]**3
            
        # Add the number to the running total
        total += lst[i]
        
    return total
