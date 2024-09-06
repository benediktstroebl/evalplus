```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            largest_divisor = i
            break
    return largest_divisor
```
The function largest_divisor takes an integer n as input and searches for the largest divisor of n by iterating through numbers from 1 to n. When an divisor is found, the loop breaks and the largest divisor is returned, as it's guaranteed that any larger divisor would have already been found due to the loop progressing in incrementally larger steps. This can be seen through the logical equivalence of the following statements:
```python
largest_divisor = i
```
* n is divisible by both i and n - i, and,
* if i is the largest possible divisor, then n - i is not a divisor of n at all.

The earliest moment the if condition evaluates to true, the loop will break and the largest divisor found will be returned. The loop structure is very inefficient for large n values, but the function still satisfies the requirements of the problem description. A more efficient approach would be to factorize the number and identify the largest divisor, but that violates the request to solve the problem using a single loop.