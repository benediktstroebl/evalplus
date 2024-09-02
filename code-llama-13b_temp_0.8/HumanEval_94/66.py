

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
    # The number of 9's in the sum of the digits is important
    # List comprehension to filter only integers
    lst = [int(x) for x in lst if type(x) is not str]
    prime_digits = [9] # List to keep prime digits
    for i in lst:
        # We don't need to check 0 and 1
        if i < 2:
            continue
        # Check if the number is prime
        for j in range(2, i):
            if i % j == 0:
                # if it is prime, add it to the prime_digits list
                prime_digits.append(sum(int(x) for x in str(i)))
                # This break is necessary, otherwise the prime_digits will have multiple entries
                break
    # Find the largest prime number
    largest_prime = max(prime_digits)
    # Sum its digits
    return sum(int(x) for x in str(largest_prime))


