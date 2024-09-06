```python
def is_prime(n):
    """
    Checks whether a number is prime
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
    # Convert the interval pairs to tuples
    s1, s2 = tuple(s1), tuple(s2)
    # Calculate the overlap interval
    overlap = [max(s1[0], s2[0]), min(s1[1], s2[1])]
    # Check if there is an intersection
    if overlap[0] >= overlap[1]:
        return "NO"
    else:
        # Check if the overlap length is prime
        overlap_length = overlap[1] - overlap[0] + 1
        if is_prime(overlap_length):
            return "YES"
        else:
            return "NO"
```

The function `intersection` takes two interval tuples as input and returns "YES" if the overlap between them has a prime number length and "NO" otherwise. The function `is_prime` is used to check if a given number is prime. Overall, the code's complexity is roughly O(N*log(N)), where N is the length of the overlap interval. It handles both the primality check and the interval calculation and detection efficiently.