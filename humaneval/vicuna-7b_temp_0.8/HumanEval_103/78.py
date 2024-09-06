
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
    # Handle the case when n is greater than m
    if n > m:
        return -1
    
    # Initialize the average to 0
    average = 0
    
    # Compute the average by summing up the integers from n through m and divide by the number of integers
    for i in range(n, m+1):
        average += i
    average = average / (m-n+1)
    
    # Round the average to the nearest integer and convert it to binary
    while average >= 5:
        average -= 1
        binary_string = "0" + binary_string
    while average >= 2:
        average -= 1
        binary_string = binary_string[:-1] + "0"
    while average >= 1:
        average -= 1
        binary_string = binary_string[:-1] + "0"
    binary_string = binary_string[:-1] + binary_string[-1:]
    return binary_string
