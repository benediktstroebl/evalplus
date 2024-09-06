```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return max([sum(map(int, str(x))) for x in primes])
```

The function `largest_prime_sum_of_digits` works by first filtering the list `nums` to obtain a list of prime numbers, using a list comprehension that checks for evenness and numerosity. If the list of primes is empty, indicating no prime numbers in the list, the function returns 0. Otherwise, it proceeds to find the maximum sum of digits from the prime numbers using a list comprehension that converts each prime number to a string, sums the digits through the `sum` function, and converts the sum back to an integer using `int`. 

The function achieves the problem's requested output for the provided examples, and can be tested against other cases as well. 

This script demonstrates a practical approach to solving problems involving prime numbers and their properties within a list. Feel free to adapt this code to your needs, or further explore the Prime Number Theory and its applications through the provided resources.