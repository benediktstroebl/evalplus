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
    prime_list = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_list.append(num)
            count += 1
            if count == n:
                break
    return prime_list

# Example usage
n = int(input("Enter a number: "))
print(count_up_to(n))
```

This script defines a function `count_up_to(n)` that takes an non-negative integer and returns an array of the first `n` integers that are prime numbers and less than n. The function checks each number in range from 2 to `n` and collects them in a list if they are primes and less than `n`. The `is_prime(n)` function is also provided to check if a number is prime or not.