```python
def largest_prime_sum_of_digits(nums):
    primes = [i for i in nums if is_prime(i)]
    return max(sum(map(int, str(p))) for p in primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
The function `largest_prime_sum_of_digits(nums)` uses the filter function to create a list of prime integers from the input list. The maximum sum of digits is then calculated using a generator expression within the map function, which iterates through the prime numbers and calculates the sum of the digits of each number. 

The `is_prime(n)` function determines if a given number is prime by iterating through numbers from 2 up to the square root of the input number and checking for divisibility. If the number is divisible by any integer within this range, it is not prime, otherwise, it is prime. 

You can use `is_prime()` as a standalone function for prime number checking, and `largest_prime_sum_of_digits(nums)` to find the largest prime sum of digits. 

The approach ensures that the prime checking process is efficient by avoiding unnecessary iterations for larger numbers.