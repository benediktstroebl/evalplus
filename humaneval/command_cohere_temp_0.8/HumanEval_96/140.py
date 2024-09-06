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
    numbers = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            numbers += [i]
            count += 1
            if count == n:
                break
    return numbers
```
The script contains two functions. The `is_prime` function checks if a given number is prime or not using a simple iterative technique that checks if the number is divisible by any number from 2 to the square root of the number. 

The `count_up_to` function uses the `is_prime` function to generate the list of prime numbers less than `n` and stores it in the `numbers` variable. It stops after adding `n` numbers to the list, or it will return more than `n` primes if there are less than `n` prime numbers available. 

The code is self-contained and can be executed directly to test it. You can also use it as a part of a larger project to solve this particular problem. 

If you need to modify the code, consider adding comments on top of each function for a better understanding of each code segment.