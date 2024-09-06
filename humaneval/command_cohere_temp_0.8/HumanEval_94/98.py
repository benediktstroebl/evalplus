```python
def largest_prime_sum_of_digits(nums):
    """Returns the largest prime sum of digits for a list of integers."""
    primes = [True for n in nums]
    # Mark non-primes
    for n in range(2, int(len(nums)**0.5)+1):
        if primes[n]:
            for i in range(n, len(nums)):
                if nums[i] % n == 0:
                    primes[i] = False
    # Find the largest prime
    largest_prime = 0
    for n in range(len(nums)):
        if primes[n] and nums[n] > largest_prime:
            largest_prime = nums[n]
    # Return the sum of the digits of the largest prime
    return sum(map(int, str(largest_prime)))
```

The algorithm consists of two parts:
1. The first part uses a simple algorithm to determine if a number is prime or not. It iterates through all the numbers from 2 to the square root of the length of the list, and for each number, it checks if it is marked as prime. If it is, it then checks if any of the subsequent numbers in the list are divisible by it. If they are, it marks them as not prime. 
2. The second part of the algorithm finds the largest prime number in the list. It initially sets the largest prime to the first number in the list, then it iterates through the list and compares the current number with the largest prime found so far. If the current number is larger and is prime, it updates the largest prime. 

The function then returns the sum of the digits of the largest prime number found. The code is self-contained and does not rely on any external modules or libraries other than the standard library. 

This solution has a time complexity of O(n^1.5) due to the square root decomposition in the first part of the algorithm, and the second part operates in linear time.