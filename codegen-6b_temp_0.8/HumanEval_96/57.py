
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
    # Note: Iteration through the count_up_to function is O(n), which is almost certainly the
    # best possible (with a BONUS of O(1) if n >> m) if the prime numbers are not actually
    # stored in memory, where m << n.
    # If the prime numbers are not stored in memory, the expected runtime is O(n log n)
    # instead, but this depends on the implementation.

    primes = primes_upto(n)

    # Find the number of times each prime is found in the list
    nums = defaultdict(int)
    for num in primes:
        while num < n:
            nums[num] += 1
            num += 1

    # Return the primes that are found N times
    return [prime for prime, count in nums.items() if count == n]

