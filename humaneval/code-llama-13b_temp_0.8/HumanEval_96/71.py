
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
    # What is the most naive solution you can think of?
    # A brute force solution would be to iterate over every number and check if they are prime.
    # This would be O(n^2)
    # Can we do better?
    # Hint: Think about the properties of prime numbers. If a number is not prime, then it's divisible by something
    # less than n. You can optimize your solution to O(n).

    # 1. Solution is a brute force solution
    primes = []
    if n <= 1:
        return primes

    for candidate in range(2, n):
        for div in range(2, candidate):
            if candidate % div == 0:
                break
        else:
            primes.append(candidate)
    return primes


    # 2. Solution uses a sieve
    # Create a list of booleans of size n. Set all the values to True (which means all numbers are initially prime)
    # Then for every multiple of the numbers, change the corresponding boolean in the list to False.
    # Then at the end return the list of numbers where the boolean values are True.
    # This solution is O(n)
    # Time complexity: O(n) because we create the sieve list and iterate over it.
    # Space complexity: O(n) because we create a list of booleans for the entire range of numbers we want to check.
    # primes = [True] * n
    #
    # for i in range(2, n):
    #     if primes[i]:
    #         for j in range(i * i, n, i):
    #             primes[j] = False
    #
    # return [i for i in range(2, n) if primes[i]]

    # 3. Solution uses a sieve
    # This is the more compact solution
    # Time complexity: O(n * log(log(n)))
    # Space complexity: O(n)
    # primes = [True] * n
    #
    # for i in range(2, int(n ** 0.5) + 1):
    #     if
