Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n + 1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes

# Test Cases
case0 = count_up_to(0)
case1 = count_up_to(1)
case2 = count_up_to(5)
case3 = count_up_to(11)
case4 = count_up_to(20)
case5 = count_up_to(18)

print(case0)  # []
print(case1)  # []
print(case2)  # [2, 3]
print(case3)  # [2, 3, 5, 7]
print(case4)  # [2, 3, 5, 7, 11, 13, 17, 19]
print(case5)  # [2, 3, 5, 7, 11, 13, 17]
```

This script defines a function `count_up_to(n)` that takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. The function counts through integers from 2 up to `n`, adding each prime number to the array until the count reaches `n` or exceeds it. The `is_prime` function is also provided to check if a number is prime.

The example outputs show the first `n` prime numbers for each test case, confirming the behavior described in the problem statement.