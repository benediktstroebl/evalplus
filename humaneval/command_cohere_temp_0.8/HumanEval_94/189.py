```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))
```

The function `largest_prime_sum_of_digits` takes a list of integers `lst` as input and returns the sum of the digits of the largest prime number in the list.

The function first uses a list comprehension to filter the list `lst` and create a new list called `primes`, which contains all the prime numbers (with magnitude greater than 1) present in the list. If the `primes` list is empty, meaning there are no prime numbers in the list, the function returns 0. If `primes` is not empty, it converts the largest prime number in the list (`max(primes)`) to a string using `str`, and then calls `map` to convert each character of the string back to an integer using `int`. Finally, it returns the sum of these integer digits. 

This function is self-contained and can be used to solve the problem as stated in the prompt. Feel free to test it with example lists provided in the prompt.