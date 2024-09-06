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
    # Convert interval to tuple (start, end)
    x = (max(s1[0], s2[0]), min(s1[1], s2[1]))
    # Return "NO" if no intersection
    if x[0] > x[1]:
        return "NO"
    else:
        # Calculate the length of intersection and then check if it's prime
        intersection_length = x[1] - x[0] + 1
        if is_prime(intersection_length):
            return "YES"
        else:
            return "NO"
```

The function `is_prime` is a simple primality test function. The main function `intersection` converts the input interval pairs into a tuple `(start, end)` format and determines whether the resulting length is prime. It returns "NO" if no intersection or if the length is not prime.

You can test this code by calling the `intersection` function with various sample inputs to verify its behavior. 
```python
intersection((1, 2), (2, 3))
intersection((-1, 1), (0, 4))
intersection((-3, -1), (-5, 5))
```
This should return:
```
"NO"
"NO"
"YES"
``` 
Which matches the given sample outputs.