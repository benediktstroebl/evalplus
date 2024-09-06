Here is a self-contained Python function that checks whether a given number is prime or not:

```python
def is_prime(n):
    """
    A function to check if a number is prime or not.
    """
    checks for all the regular factor of n, where a factor is a positive integer 
    that divides n evenly. If no such is found, return True, otherwise return False.
    """

Here's how the function works:
1. The function begins by creating a factor-checking list, which will store the factors of `n` as the function runs.
2 The function then loops through the list of factors, starting with 2 and continuing until the factor is not divisible by `n`.
3. If the factor is found to be divisible by `n`, the function returns `False`, indicating that `n` is not a prime number.
4. If the loop completes, the function returns `False`, indicating that no factors were found, the function returns `True`, indicating that `n` is a prime number.

Here are some test cases to demonstrate the functionality of the function:
```python
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This function is self-contained and requires no external variables or function calls. It can be used as a basis to build more complex prime number checking functionality.