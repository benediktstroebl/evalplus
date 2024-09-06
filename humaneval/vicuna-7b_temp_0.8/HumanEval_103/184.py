
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
    # Check if n is greater than m
    if n > m:
        return -1
    
    # Convert n and m to binary
    n_bin = str(n)[2:]
    m_bin = str(m)[2:]
    
    # Get the number of digits in the binary representation of n
    digits_n = len(n_bin)
    
    # Calculate the average by adding up the digits of n and m and dividing by the number of digits
    total = n_bin + m_bin
    average = (n + m) // digits_n
    
    # Convert the average to binary and round it to the nearest integer
    average_bin = str(int(average)).zfill(digits_n)
    
    # Return the result
    return average_bin
