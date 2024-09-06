```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    sqrts = [int(n**0.5) for n in nums]
    max_prime = 0
    for i, n in enumerate(nums):
        if primes[i] and sqrts[i] * sqrts[i] == n:
            max_prime = i
        elif not primes[i] and n >= 10:
            sum_digits = sum(map(int, str(n)))
            if sum_digits > max_prime:
                max_prime = sum_digits
    return max_prime
```
The function iterates through the list of integers, marking whether each number is prime or not. Then, for potential prime numbers, it calculates their square root to compare if the number is a perfect square, and updates the `max_prime` variable if needed. Finally, if a number is not prime, it sums the digits of the number to compare this sum with the `max_prime` found so far, updating it if necessary. This way, the function finds the largest prime number in the list and returns the sum of its digits.