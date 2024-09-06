```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
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

The function `is_prime` is used to check if a number is prime. Then, the function `count_up_to` starts counting from 2 up to *n* and stores each prime number in the primes list until it has collected *n* primes or exceeded *n*, whichever occurs first.

This solution includes the unit test cases to verify the correctness of the `is_prime` and `count_up_to` functions. You can use the following code to test these functions:
```python
# Testing the prime number checking function
print(is_prime(0)) # Should print False
print(is_prime(1)) # Should print False
print(is_prime(2)) # Should print True
print(is_prime(3)) # Should print True
print(is_prime(4)) # Should print False
print(is_prime(5)) # Should print True
print(is_prime(6)) # Should print False

# Testing the count_up_to function
print(count_up_to(5))  # Should print [2, 3]
print(count_up_to(11))  # Should print [2, 3, 5, 7]
print(count_up_to(0))  # Should print []
print(count_up_to(20))  # Should print [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # Should print []
print(count_up_to(18))  # Should print [2, 3, 5, 7, 11, 13, 17]
```

This will help you verify the correctness of the solution.