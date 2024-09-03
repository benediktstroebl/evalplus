```python
def is_prime(n):
    """
    Checks whether a positive integer 'n' is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Checks whether the length of the intersection of two given intervals is a prime number or not.
    """
    # Convert interval to python intervals
    start1, end1 = s1
    start2, end2 = s2
    
    # Calculate the intersection
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)
    
    # Check if there is an intersection
    if intersect_start > intersect_end:
        return "NO"
    
    intersect_length = intersect_end - intersect_start + 1
    
    if is_prime(intersect_length):
        return "YES"
    else:
        return "NO"
```

The function utilizes the `is_prime` helper function to determine whether the length of the intersection of two given intervals is a prime number or not. The `is_prime` function checks if a given number is less than or equal to one, it returns False; and for the range of 2 up to the square root of the number, it checks whether the number is divisible or not. If the number is divisible, it returns False; otherwise, it returns True. 

The function then returns "YES" if the length of the intersection is prime; otherwise, it returns "NO". If the two intervals don't intersect, the function returns "NO". The script passes the provided tests.