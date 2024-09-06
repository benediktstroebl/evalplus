

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

    # The numbers that are the potential largest prime numbers
    # are the ones which are greater than the largest digit
    largest_number = max(lst)

    # The largest digit is the maximum of the number
    largest_digit = max(str(largest_number))

    # The maximum number of digits is the number of digits of the largest digit
    maximum_number_of_digits = len(str(largest_digit))

    # The maximum number that can be represented by the maximum number of digits
    # is the largest number whose digits are all the largest digits.
    maximum_number = int("9" * maximum_number_of_digits)

    # The maximum prime number is the greatest of the maximum numbers
    maximum_prime_number = max(x for x in lst if x <= maximum_number)

    # Add the digits of the maximum prime number
    return sum(int(x) for x in str(maximum_prime_number))








