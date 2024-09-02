
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
    if n > m:
        return -1
    elif n == m:
        return bin(n)
    else:
        # Generate the list of numbers
        number_list = []
        for i in range(n, m + 1):
            number_list.append(i)
        # Average the numbers
        mean = sum(number_list) / len(number_list)
        # Round and convert to binary
        mean = round(mean)
        mean = bin(mean)
        # Return the binary value
        return mean

