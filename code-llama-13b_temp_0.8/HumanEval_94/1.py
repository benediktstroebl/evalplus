

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
    import numpy as np
    from collections import Counter
    
    # return the largest prime number in list lst
    # Calculate the largest prime number in a given list of integers.
    # lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    prime_lst = []
    for num in lst:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_lst.append(num)

    #print(prime_lst)
    if not prime_lst:
        return 0
    else:
        largest = max(prime_lst)
    #print(largest)
    # calculate the sum of the digits in the largest prime number
    # 25 = 1+2+5
    # largest = 10
    # sum of digits = 1+0 = 1
    sum_of_digits = sum([int(num) for num in str(largest)])

    return sum_of_digits






















