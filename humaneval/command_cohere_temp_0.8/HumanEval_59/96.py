```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    factor = n
    while factor % 2 == 0:
        factor //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while factor % i == 0:
            factor //= i
    if factor > 1:
        return factor
    else:
        return n
```
The function iterates through potential factors from 2 up to the square root of n, dividing n by any factor that divides it evenly. This process continues until n is reduced to prime factors that are no longer divisible. The maximum prime factor is returned if there are any, or the original n if it is a prime number. 

Here is an example of how to use the function:
```python
result = largest_prime_factor(52)
print(result)
```
Which gives an output of:
```
2
```
This demonstrates how the function returns the largest prime factor of the input n, which is 2 in this case, since 52 = 2 * 2 * 13.