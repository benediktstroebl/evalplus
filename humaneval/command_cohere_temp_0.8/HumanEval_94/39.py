```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = nums[0]
    max_sum = nums[0]
    for n in nums:
        if primes[n]:
            if n > max_prime:
                max_prime = n
        else:
            for digit in str(n):
                if int(digit) > max_sum:
                    max_sum = int(digit)
        primes[n] = False
    return max_sum
```
The function `largest_prime_sum_of_digits` works by first initializing an array of boolean values (`primes`) and setting `max_prime` and `max_sum` to the first element of the input list. The loop iterates through the list and for each element, it checks if it's prime. If it is, it compares it to `max_prime` and updates it if needed. For non-prime numbers, it iterates through their digits and updates `max_sum` if necessary. Finally, the function returns `max_sum`, which represents the largest prime value's digit sum from the input list. 

Here's a simpler solution using the `prime` library:
```python
import prime

def largest_prime_sum_of_digits(nums):
    return sum(n for n in nums if prime.is_prime(n))
```
This solution leverages the `prime.is_prime` function to iterate through the list and calculate the sum of prime numbers.