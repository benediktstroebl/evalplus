

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

    # generate prime numbers
    lst_primes = [2]
    cur_prime = 3
    while cur_prime < max(lst):
        for p in lst_primes:
            if cur_prime % p == 0:
                break
        if cur_prime not in lst_primes:
            lst_primes.append(cur_prime)
        cur_prime += 2

    # check for each prime if there is a match in the list
    max_digit_sum = 0
    for prime in lst_primes:
        if prime in lst:
            digit_sum = sum([int(d) for d in str(prime)])
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum

    return max_digit_sum

