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
n = 5
print(count_up_to(n))
```

This script defines a function `count_up_to(n)` that takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. The function iterates through integers from 2 up to `n`, checking each integer with the `is_prime` function to determine if it is prime. If the integer is prime and less than `n`, it is added to the `prime_list`, and the `count` variable is incremented. The loop stops when `count` reaches `n`, ensuring that the function returns the correct number of prime numbers as specified by `n`. 

The `is_prime` function is also included in the script. It is a necessary step for checking whether an integer is a prime number, and it is used as a utility function in the `count_up_to` function.

An example usage is provided in the script, where the `count_up_to` function is called with `n = 5`, and the resulting array [2, 3] is printed as output.