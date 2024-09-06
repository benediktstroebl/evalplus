

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
    # Step 1: Create the list of primes
    prime_lst = []
    for i in lst:
        # Step 2: Make a list of numbers divisible by the current number
        # (i.e., all the numbers in the list that are not prime)
        nonprime_lst = []
        for j in lst:
            if i > 0:
                if j % i == 0:
                    nonprime_lst.append(j)
                else:
                    continue
            else:
                continue
        # Step 3: Remove all numbers in nonprime_lst from lst
        for k in nonprime_lst:
            lst.remove(k)
        # Step 4: Append the number to prime_lst
        prime_lst.append(i)
    # Step 5: Sum the numbers in prime_lst
    # Hint: Use sum(lst)
    s = sum(prime_lst)
    # Step 6: Sum the digits of the total
    return sum([int(i) for i in str(s)])

