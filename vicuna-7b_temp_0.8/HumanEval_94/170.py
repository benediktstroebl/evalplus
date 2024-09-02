

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
    # The largest prime
    largest = 0
    prime = True
    for num in lst:
        if not num % 2 and num > 1:
            # Check the number of digits in the number
            num_digits = len(str(num))
            # Update the largest prime and prime
            if num_digits > largest:
                largest = num_digits
                prime = True
            elif num_digits == largest and not prime:
                prime = True
    # The sum of digits
    sum = 0
    # The sum of digits of the largest prime
    for i in range(largest):
        sum += int(str(largest)[i])
    return sum