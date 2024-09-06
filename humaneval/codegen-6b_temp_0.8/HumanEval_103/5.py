
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
    # You will need to use a while loop here to implement the
    # method. One iteration will be done for you, you must implement the while
    # loop.
    

    # TODO: Implement your function here. Use the def for this question.
    #
    # This is the rounded_avg(n, m)
    n, m = int(n), int(m)
    if n > m:
        return -1
    else:
        result = (m + n - 1) // 2
        answer = bin(result)[2:]
        return answer
