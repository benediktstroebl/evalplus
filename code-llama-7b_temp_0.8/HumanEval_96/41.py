
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    #Step 1: Initialize list of primes
    primes = []

    #Step 2: Add 2 to the list of primes
    primes.append(2)

    #Step 3: Initialize a count variable
    count = 2

    #Step 4: Initialize a divisor
    divisor = 3

    #Step 5: Loop through all integers less than or equal to n
    while divisor <= n:

        #Step 6: If the divisor is a factor of the count, it is not prime.
        if divisor % count == 0:

            #Step 7: Increment divisor by 2
            divisor += 2
        else:

            #Step 8: Add the divisor to the list of primes
            primes.append(divisor)

            #Step 9: Increment count and divisor by 1
            count += 1
            divisor += 1

    #Step 10: Return the list of primes
    return primes

