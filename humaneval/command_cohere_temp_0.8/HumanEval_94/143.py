```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if is_prime(x)]
    return max(map(sum_of_digits, primes))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    return sum(int(d) for d in str(n))
```
The function `largest_prime_sum_of_digits(nums)` returns the largest sum of digits among the largest prime numbers in the list `nums`. The function `is_prime(n)` checks if a number is prime using a optimized loop, and the function `sum_of_digits(n)` calculates the sum of the digits of a number. When the given examples are tested against this function, it passes all of them. 
Here is an example of using this function:
```python
print(largest_prime_sum_of_digits([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]))
```
Which prints out:
```bash
10
```

This is consistent with the provided example in the problem statement.