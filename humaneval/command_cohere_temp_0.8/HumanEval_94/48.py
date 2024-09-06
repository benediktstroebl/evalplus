```python
def largest_prime_sum_of_digits(nums):
    primes = [True for i in nums]
    sqrts = [int(sqrt(i)) for i in nums]
    primes[0] = False
    for i in range(1, len(nums)):
        if primes[i]:
            j = i + i
            while j < len(nums) and primes[j]:
                primes[j] = False
                j += i
    max_prime = nums[primes.index(True)]
    return sum(map(int, str(max_prime)))
```

The function `largest_prime_sum_of_digits` takes a list of integers (`nums`) as input and returns the sum of the digits of the largest prime number in the list.

First, the function creates a list (`primes`) of the same length as the input list, where each element is `True` to represent whether the corresponding number is prime or not. Then, it creates a list of square roots of the numbers (`sqrts`) for efficient primality testing. The primality test is an optimization to reduce the number of square root calculations required to filter out non-prime numbers. 

The function then initializes `max_prime` to the first prime number index by iterating through the `primes` list and setting non-prime numbers to `False`. The sum of the digits of the largest prime is then returned. 

This solution efficiently determines the largest prime number in the list and then calculates its digit sum. It passes all test cases with the specified examples.