```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The function `count_up_to()` leverages the `is_prime()` function to solve the problem. It iterates through numbers from 2 up to `n`, storing every prime number that is less than `n` in the `primes` list. The `count` variable keeps track of the amount of primes found. Once `count` reaches `n`, the function stops iterating. Lastly, it returns `primes`, which is an array of the first `n` prime numbers less than `n`. 

You can test this implementation using the following code:
```python
Test().mount("CountUpTo")
test = CountUpToTestCase(count_up_to)
test.test_count_up_to_5()
test.test_count_up_to_11()
test.test_count_up_to_0()
test.test_count_up_to_20()
test.test_count_up_to_1()
test.test_count_up_to_18()
Test().unmount("CountUpTo")
```

This will run multiple test cases on the function to ensure its correctness.