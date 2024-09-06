```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number.
    """
    # Convert interval to integers
    s1, s2 = map(int, s1), map(int, s2)
    # Calculate the intersection length (integer)
    x = max(s1[1], s2[1]) - min(s1[0], s2[0])
    # Check if the intersection length is prime
    if is_prime(x):
        return "YES"
    else:
        return "NO"
```

The approach used by the function `intersection()` above is as follows:
1. Convert the interval pairs to integer intervals, so that the intervals are well-defined.
2. Calculate the length of the intersection of the two intervals using `max(s1[1], s2[1]) - min(s1[0], s2[0])`.
3. Check if the length of intersection is prime using the `is_prime()` function.
4. Return "YES" if the length of intersection is prime, otherwise return "NO".

The `is_prime()` function is a simple primality test checking if a number is less than or equal to 1, it returns False; if the number is greater than 1, it iterates from 2 to the square root of the number and checks if the number is divisible by any integer in this range, if it is, it returns False.  If the loop completes without finding a divisor, it returns True.

This code is packaged in a self-contained Python script, excluding the test cases, which can be directly executed to see the function's behavior against different test cases. 

Ensure that the intervals are passed as tuples like `(start, end)`. The code employs type conversion to handle other data types appropriately.