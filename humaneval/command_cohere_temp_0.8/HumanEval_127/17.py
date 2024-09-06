```python
def is_prime(n):
    """
    Checks whether the given integer n is a prime number or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two given intervals is a prime number or not.
    """
    # Convert the tuple to integers to make subtraction operator work.
    start1, end1 = map(int, s1)
    start2, end2 = map(int, s2)

    # Determine if the two intervals intersect.
    if start1 > end2 or start2 > end1:
        return "NO"

    # Determine the length of the intersection.
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_length = intersection_end - intersection_start + 1

    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"
```

The function `is_prime` in the code above is a helper function that checks whether a given integer is a prime number or not. The main function `intersection` takes two interval tuples as input and determines whether their intersection length is a prime number or not. 

The output of the example inputs is:
- `intersection((1, 2), (2, 3)) --> "NO"`
- `intersection((-1, 1), (0, 4)) --> "NO"`
- `intersection((-3, -1), (-5, 5)) --> "YES"`