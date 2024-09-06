```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to retain only the prime numbers. It then calculates the digit sum for each prime number and returns the maximum digit sum among them.

To filter out the prime numbers from `lst`, the function utilizes a list comprehension with a condition. This condition checks that each element `x` in `lst` is greater than 1 and simultaneously, when iterating through numbers from 3 to the square root of `x` (inclusive), each `x` is not divisible by any of those numbers `n` (with an exception for odd numbers, as they are not divisible by 2). After the pruning, the list of prime integers remains.

The digit sum of a number is achieved by converting it to a string and summing the resulting integers. As the maximum function operates in parallel on multiple strings, the `map(int, ...)` call is used to ensure the sum operation works on numbers and not strings, which would result in an error. The maximum digit sum is then returned as the function result.