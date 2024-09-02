

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    # Find the largest prime number in the list
    max_val = max(lst)
    max_digit = 0
    
    # Find the sum of digits
    sum = 0
    for num in lst:
        sum += num % 10
    
    # Keep updating the sum of digits
    while max_val > 0:
        if max_val % 2 == 0:
            max_digit += sum % 10
            max_val /= 2
            sum = (sum / 10) % 10
        else:
            max_digit += sum % 10
            max_val /= 3
            sum = (sum / 10) % 10
    
    # Return the sum of digits
    return max_digit

lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
result = skjkasdkd(lst)
