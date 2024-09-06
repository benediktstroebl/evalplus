```python
def is_prime(n):
    """
    Checks whether a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def intersection(s1, s2):
    """
    Determine whether the length of the intersection of two closed intervals is prime
    """
    # Convert interval to Python's range object
    r1 = range(s1[0], s1[1] + 1)
    r2 = range(s2[0], s2[1] + 1)

    # Find the intersection by sorting and comparing
    intersection = list(set(r1) & set(r2))

    # Check if no intersection and return N
    if not intersection:
        return "NO"

    # Check if the length of the intersection is prime
    if is_prime(len(intersection)):
        return "YES"
    else:
        return "NO"
```

The script utilizes two primary components:
1. The `is_prime` function: Harnessing a fundamental primality testing algorithm, this function assesses whether a given number is prime or not. It's essential for the primality check of the length of the intersection.
2. The `intersection` function: This function is the main executional body of the code. It transforms the given interval specifications into Python's range objects, subsequently sorting and comparing these ranges to deduce the intersection. The function scrutinizes whether the intersection is empty or not, subsequently calling `is_prime` to assess the primality of the intersection's length. 

The function performs the task statement accordingly and returns "YES" if the intersection length is prime and "NO" otherwise. The logic also accounts for scenarios where the intervals do not intersect, thus returning "NO."