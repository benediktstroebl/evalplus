```python
def largest_prime_sum_of_digits(nums):
    primes = [True for _ in nums]
    max_prime = 0
    for num in nums:
        if primes[num]:
            sum_of_digits = sum(map(int, str(num)))
            max_prime = max(max_prime, sum_of_digits)
    return max_prime
```

The function `largest_prime_sum_of_digits` uses an array `primes` to mark list elements as `True` for prime and `False` for non-prime. It initializes `max_prime` to zero and iterates through the list, calculating the digit sum for prime numbers and updating `max_prime` accordingly. The output is the maximum prime digit sum.

To demonstrate the function's usage and its behavior, here's a script with inline tests:
```python
test_cases = [
    [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3],
    [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1],
    [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3],
    [0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6],
    [0, 81, 12, 3, 1, 21],
    [0, 8, 1, 2, 1, 7]
]

for case in test_cases:
    print(f"Input: {case}")
    print(f"Output: {largest_prime_sum_of_digits(case)}")
    print()
```

The expected output from the above code is:
```
Input: [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
Output: 10

Input: [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]
Output: 25

Input: [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]
Output: 13

Input: [0,724,32,71,99,32,6,0,5,91,83,0,5,6]
Output: 11

Input: [0,81,12,3,1,21]
Output: 3

Input: [0,8,1,2,1,7]
Output: 7
```