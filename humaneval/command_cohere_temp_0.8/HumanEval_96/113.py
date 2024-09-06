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
    prime_numbers = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            prime_numbers.append(i)
            count += 1
            if count == n:
                break
    return prime_numbers
```

This script defines the `count_up_to()` function, which takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. The `is_prime()` function is used to check if a number is prime. The `count_up_to()` function iterates through numbers from 2 up to `n`, adding each prime number to the `prime_numbers` list until the list has `n` elements, which is then returned.

Here is a sample output of the function:
```python
count_up_to(5) => [2, 3]
count_up_to(11) => [2, 3, 5, 7]
count_up_to(20) => [2, 3, 5, 7, 11, 13, 17, 19]
```

This script provides a solution to the problem and demonstrates the use of lists and loops, as well as a simple prime number checking function.