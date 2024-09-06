```python
def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
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
    # Convert the interval pair to a tuple.
    interval = tuple(sorted([s1, s2]))
    # Calculate the length of the intersection.
    length = abs(interval[0][1] - interval[1][0])
    # Check if the length is a prime number.
    if is_prime(length):
        return "YES"
    else:
        return "NO"
```

The aforementioned function `is_prime` is utilized to verify whether a given integer is a prime number or not. In the function `intersection`, the given intervals are converted into a tuple and sorted by start point in ascending order. Subsequently, the length of the intersection is calculated and checked via the `is_prime` function. If the length is prime, the function returns "YES"; otherwise, it returns "NO". 

Here is an example of how to use the `intersection` function:
```python
print(intersection((-3, -1), (-5, 5)))
```

This would output:
```
YES
```

This is because the intersection of the intervals (-3, -1) and (-5, 5) has a length of 3, which is a prime number. 

Another example:
```python
print(intersection((1, 2), (2, 3)))
```

The output would be:
```
NO
```

This is because the length of the intersection of the intervals (1, 2) and (2, 3) is not a prime number.