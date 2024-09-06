```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % d for d in range(3, int(x**0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It uses a generator expression to filter out prime numbers from the list, then maximizes the sum of digits of the largest prime number using a list comprehension and finally returns the maximum sum.

To get the largest prime number in the list the filter processes the list iteratively excluding numbers that are divisible by any odd number from 3 to the square root of the number, which are all prime numbers greater than 3. The list comprehension sums the digits of each prime number, and the max function returns the largest sum among them.