def starts_one_ends(n):
    # Create a list to store the results for  numbers that start or end with 1.
    ones = [1] * n
    
    # Add the count of numbers that start with 1.
    ones[0] = 0
    
    # Add the count of numbers that end with 1.
    ones[-1] = 0
    
    # Initialize the count of numbers that start or end with 1.
    count = ones.count(0)
    
    return count