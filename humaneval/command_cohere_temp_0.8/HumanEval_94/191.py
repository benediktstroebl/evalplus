```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(map(int, str(max_prime)))
```

The provided Python code defines a function called skjkasdkd that takes a list of integers as input. First, it filters the list to retain only the prime numbers greater than 1 using a list comprehension. It calculates the maximum prime value among these filtered prime numbers using the max() function. If no prime numbers are found, it sets the maximum prime to 0. Finally, it converts the maximum prime number to a string, sums the digits of that string using map(int, ...) to ensure the sum is computed as an integer, and returns the resulting digit sum. This approach ensures that it finds the maximum prime number in the list and then calculates the sum of its digits.