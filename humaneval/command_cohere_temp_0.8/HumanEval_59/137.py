```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Make a list of the prime factors of n
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n //= i
    if n > 2:
        pf.append(n)
    # Return the largest factor
    return max(pf)
```
The function largest_prime_factor() takes an integer n as input and returns the largest prime factor of n. This algorithm repeatedly divides the number n by the smallest prime factor that remains, starting from 2 and moving up through the number's square root. The smallest prime factor is chosen because there may be multiple factors of the number, and dividing by a larger prime factor would eliminate the smaller ones. Once a number is divided enough to become 1, the loop ends. Any remaining prime factors will be greater than the square root of the original number, so the loop will not iterate through them. The function then returns the largest factor identified. 

Here is an example of the previously failed test case, 2048, to demonstrate that the problem is solved:
```python
largest_prime_factor(2048)
```
The output will be:
```
2
```

This is the expected largest prime factor of the input 2048.