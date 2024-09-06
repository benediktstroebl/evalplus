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
    """Return an array of the first n prime numbers less than n."""
    ans = []
    for i in range(2, n + 1):
        if is_prime(i) and i < n:
            ans.append(i)
    return ans
```
The `count_up_to()` function iterates through numbers from 2 up to `n`, adding each prime number less than `n` to the `ans` array until it reaches the desired length of `n`. This approach ensures that the function fulfills the problem requirements, generating the desired prime number arrays for different input values of `n`. 
The `is_prime()` function is reused from previous responses and correctly checks whether a given number is prime or not, which is essential for the `count_up_to()` function to work correctly.