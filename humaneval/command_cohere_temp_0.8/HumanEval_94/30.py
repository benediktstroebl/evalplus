```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x >= 2 and all(x % d for d in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` takes a list of integers (`lst`) as input. It filters out the prime numbers from the list using a generator expression, then finds the maximum sum of digits among those prime numbers. The generator expression employs the `all` function and the range function to efficiently determine whether each element is divisible by any number from 3 to its square root, thereby identifying prime numbers. Finally, the function converts each prime number to a string, sums up its digits, and finds the maximum sum among them. The final result is the maximum digit sum among the prime numbers in the list.