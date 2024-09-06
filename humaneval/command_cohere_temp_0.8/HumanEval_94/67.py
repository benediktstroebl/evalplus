```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))]
    return max(sum(map(int, str(x))) for x in primes)
```

The function `largest_prime_sum_of_digits` works by first filtering the list `lst` to obtain a list of prime integers using the condition `x > 1 and all(x % n for n in range(3, int(x ** 0.5) + 1, 2))`. The function then calculates the digit sum for each prime number, converts each prime number to a string to be able to access its individual digits, and sums the digits using the `sum` function and `map` argument. The `map` function is used to convert each character in the string representation of the prime number to an integer. Finally, the maximum digit sum is returned, as the task requires.