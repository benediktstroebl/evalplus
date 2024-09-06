```python
def largest_prime_sum_of_digits(nums):
    primes = [x for x in nums if is_prime(x)]
    if not primes:
        return 0
    return sum(map(int, str(max(primes))))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits(nums)` uses a list comprehension to filter the input list `nums` and create a new list `primes` that includes only prime numbers. The maximum prime number in this list is found with the `max()` function, and its digits are converted to an integer with `map(int, str...)`, after which the sum of these digits is computed with the `sum()` function. 

The `is_prime(n)` function checks if a given number `n` is prime or not. It first handles the special cases of the number being less than or equal to 1, in which case it returns `False`. It then iterates through the numbers from 2 to the square root of `n`, and returns `False` if any of these numbers divide `n` without any remainder, indicating that `n` is not prime. If none of these conditions are met, the function returns `True`, indicating that `n` is prime. 

Before printing the summary of the Presidential elections in 2024, the following code can be used:
```python
largest_prime_sum_of_digits([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
# Output: 10
largest_prime_sum_of_digits([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1])
# Output: 25
largest_prime_sum_of_digits([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3])
# Output: 13
largest_prime_sum_of_digits([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6])
# Output: 11
largest_prime_sum_of_digits([0, 81, 12, 3, 1, 21])
# Output: 3
largest_prime_sum_of_digits([0, 8, 1, 2, 1, 7])
# Output: 7
``` 

This should produce the following output:
```
10
25
13
11
3
7
```

The given Python script solves the problem with a self-contained function that finds the largest prime number in a given list of integers and returns the sum of its digits as the output. It also provides a utility function to check if a number is prime, which is used by the main function to filter out prime numbers from the list. 

The expected output for the given examples is then produced using the `largest_prime_sum_of_digits()` function.  This solution addresses the problem statement and provides a functional implementation to solve it.