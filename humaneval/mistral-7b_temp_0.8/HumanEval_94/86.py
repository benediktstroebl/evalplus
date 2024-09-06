

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
    # consider lst[0] as prime number and get the max from it
    # consider all the numbers in the list to be factors
    # divide the max number by factors
    # keep checking the factors and adding to max number
    # if the max number is prime, then add it to the sum of its digits
    # if not, then continue to divide by the factors
    # if max number is prime and all factors are exhausted, then return the sum of the digits
    # if max number is not prime, then continue with next number

    prime_num = lst[0]
    max_num = lst[0]
    sum_of_digits = 0

    for num in lst:
        if prime_num < num:
            prime_num = num

    for num in lst:
        while num % prime_num == 0:
            num = num / prime_num
            sum_of_digits += sum(str(prime_num))

    return sum_of_digits
