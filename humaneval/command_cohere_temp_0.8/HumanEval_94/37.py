```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % d for d in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` uses a list comprehension to filter the list `lst` and create a new list `primes` that contains only the prime numbers. The function then uses a generator expression to convert each prime number to a string and sum the digits. Finally, `max` is used to find the largest sum of digits amongst the prime numbers.

Here is a more detailed breakdown of the code:
- `x >= 2`: Filters out all numbers that are less than 2, as prime numbers must be greater than 2.
- `all(x % d for d in range(3, int(x**0.5) + 1, 2))`: This line checks if `x` is divisible by any number in the range `[3, int(x**0.5) + 1]`. 
    - `x**0.5` calculates the square root of `x`.
    - Adding 1 to the square root ensures that the loop includes the number itself (`x`).
    - The loop iterates in steps of 2, i.e., it checks only odd numbers, as divisors of primes are either 1 or prime numbers themselves.
- `max(sum(map(int, str(x))) for x in primes)`: This line calculates the sum of digits of each prime number in the `primes` list, converts it to an integer, and finds the maximum value. 

The function returns the largest sum of digits of a prime number in the given list.