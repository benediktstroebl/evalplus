```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It uses a list comprehension to filter out prime numbers from the list, then maximizes the sum of digits for the largest prime number found. The filtering process looks for integers greater than 1 and verifies that each number is divisible only by 1 and itself (i.e., it's prime) by iterating from 3 up to the square root of the number, skipping every other number. The result is the maximum digit sum of the largest prime numbers in the list.