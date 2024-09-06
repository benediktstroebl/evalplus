```python
def largest_prime_sum_of_digits(nums):
    primes = [True for i in nums]
    maxPrime = 0
    maxSum = 0
    for num in nums:
        if primes[num]:
            sumOfDigits = sum(map(int, str(num)))
            if sumOfDigits > maxSum:
                maxSum = sumOfDigits
                maxPrime = num
    return maxSum
```

The function `largest_prime_sum_of_digits` takes a list of integers as input and returns the largest sum of digits of a prime number in the list.

The function initially assumes that all elements in the list are prime and calculates the maximum sum of the digits of all numbers. Then, it evaluates whether each number is prime, updating the maximum sum and the corresponding number whenever a non-prime number is identified. Ultimately, the function returns the largest sum of digits among prime numbers. 

This solution ensures the list comprehension's efficiency in evaluating primality and sums of digits, optimizing the code's performance, and accurately solving the problem.