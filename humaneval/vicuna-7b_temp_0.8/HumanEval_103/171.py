
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    # Check if n > m
    if n > m:
        return -1
    
    # Initialize result to 0b0
    result = "0b0"
    
    # Loop from n to m and calculate the average
    for i in range(n, m+1):
        # Add i to the result
        result += str(i)
        
    # Convert the string to binary and round it to the nearest integer
    result = round(int(result, 2))
    
    # Convert the result to binary and return it
    return str(result)
