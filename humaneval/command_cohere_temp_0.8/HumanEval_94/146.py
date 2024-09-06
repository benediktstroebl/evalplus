```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    sqrts = [int(n**0.5) for n in nums]
    thrs = []
    for i in range(len(sqrts)):
        thrs.append(sqrts[i] + 1 if primes[i] else sqrts[i])
    return sum(map(int, str(max(thrs))))
```

The function `largest_prime_sum_of_digits` takes a list of integers (`nums`) as input and returns the sum of the digits of the largest prime number in the list.

The approach is to iterate through the list and mark non-prime numbers using their square root. The threshold is calculated as the square root of a number plus one if it's prime, or just the square root if it's not. The largest prime is found by comparing thresholds and its digits are summed using `str` and `int` functions. 

This solution has a time complexity of `O(n log n)` due to square root calculations and an additional `O(n)` for the marking non-prime numbers. The space complexity is `O(n)` due to the creation of the `thrs` list.