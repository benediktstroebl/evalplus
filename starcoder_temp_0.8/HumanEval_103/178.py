
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

    # The idea is to calculate the average of the integers from n through m (including n and m)
    # Then round the answer to the nearest integer, which will be the number of bits for the binary representation
    # Then convert that to binary
    
    # Edge case
    if n > m:
        return -1

    # First, calculate the average
    average = (n + m) // 2
    
    # Then, round to the nearest integer
    rounded = round(average)
    
    # Then, convert to binary
    binary_rep = bin(rounded)
    
    # Return the binary representation
    return binary_rep[2:]


