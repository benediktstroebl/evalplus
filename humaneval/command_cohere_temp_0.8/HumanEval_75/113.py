```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```

The function `is_multiply_prime` takes a single argument `n`, which is the number to be checked.

First, a list of known primes is imported `primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]`. These are the primes smaller than 100. Then, an efficient approach is used to find the factors of the given number `factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)`. For each integer `i` in the range, `factors` will contain `i` if `n` is divisible by `i`. This set is created using a set comprehension in Python. It will automatically remove any duplicate factors. 

Finally, the function returns `True` if the number is a product of exactly three primes and all of these primes are in the known primes list. Otherwise, it returns `False`. 

This solution has an O(n sqrt(n)) complexity, as it loops through all the numbers up to `sqrt(n)` and does an `O(1)` operation for each number, and another `O(n sqrt(n))` operation is the set comprehension to find the distinct factors. 

Note that this approach assumes the input numbers are valid integers. If the input numbers are not valid, the function may still return a correct result, but it may also raise an error depending on the specific implementation and underlying libraries. 

To handle potential issues, you may want to add additional input validation and error handling depending on your specific use case.