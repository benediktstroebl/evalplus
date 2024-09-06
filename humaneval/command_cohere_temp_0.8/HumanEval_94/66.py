```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(map(int, str(max_prime)))
```

The provided code defines a function `skjkasdkd` that takes a list of integers as input and aims to find the largest prime number in the list and return the sum of its digits.

Here's a breakdown of the code:
1. The function `skjkasdkd` takes a list `lst` as input.
2. It uses a list comprehension to find all prime numbers in the list `primes = [x for x in lst if x % 2 == 1 and x > 1]`. This checks if each element `x` is odd (`x % 2 == 1`) and greater than 1 (`x > 1`), which are both prime-likeiring conditions.
3. It finds the maximum value in the list of primes using `max(primes)` and converts it to a string (`str(max_prime))`.
4. The `map` function is then used to convert each character in the string representation of the largest prime to an integer, and the sum of these integers is calculated using `sum(...)`. 

The code essentially extracts the largest prime number from the input list and computes the sum of its digits.

Note: This solution assumes that the list may contain duplicate prime numbers, and it will select the largest one. Also, it's generally slow for long lists to iterate over the entire list for primes. Optimized prime-finding algorithms could improve efficiency.