

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

    if max(lst) > 10000:
        return None

    def isprime(num):
        # check if num is prime number
        # if yes return True else return False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            return True
        else:
            return False

    # find largest prime value from list lst
    max_prime = max(lst)
    if isprime(max_prime):
        # store all prime numbers into list prime_lst
        prime_lst = [i for i in lst if i == max_prime or isprime(i)]
        # check if prime_lst is not empty
        if prime_lst:
            # store all digits of largest prime number into list prime_lst_digits
            prime_lst_digits = [int(x) for x in str(prime_lst[0])]
            # check if prime_lst_digits is not empty
            if prime_lst_digits:
                # return sum of digits of largest prime number
                return sum(prime_lst_digits)
        return None
    else:
        return None

