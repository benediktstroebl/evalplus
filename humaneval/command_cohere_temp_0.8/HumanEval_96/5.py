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
    """Return the first n prime numbers less than n"""
    count = 0
    primes = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            primes.append(num)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to see if it's prime. If the number is prime and less than `n`, it adds it to the `primes` list and increments the `count` counter. Once `count` reaches `n`, the function stops iterating and returns the list of prime numbers.

To verify the correctness of the given implementation, let's test it with various inputs using Python's built-in `assert` statement to verify the expected output for various cases:
```python
# Basic tests
assert count_up_to(0) == []
assert count_up_to(1) == []
assert count_up_to(5) == [2, 3]
assert count_up_to(11) == [2, 3, 5, 7]

assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

# Edge case
assert count_up_to(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

You can add test cases as needed to cover more scenarios and ensure the correctness of the implementation.