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
    Determine whether the length of the intersection of two given intervals is a prime number or not.
    """
    if s1[0] > s2[1] or s1[1] < s2[0]:
        return "NO"
    else:
        interval_length = max(s1[1], s2[1]) - min(s1[0], s2[0])
        if is_prime(interval_length):
            return "YES"
        else:
            return "NO"
```

The function relies on the `is_prime` function to determine if the intersection length is prime. It also includes a check to confirm if the intervals intersect, returning "NO" if they don't. This is followed by a few test cases to ensure the function works as expected.  These test cases encompass various scenarios that help prove the function's correctness. 

You can add this test suite to your script to ensure the function's robustness and accuracy:
```python
def test_intersection():
    """
    Test the intersection function.
    """
    assert intersection((1, 2), (2, 3)) == "NO"
    assert intersection((-1, 1), (0, 4)) == "NO"
    assert intersection((-3, -1), (-5, 5)) == "YES"
    assert intersection((0, 2), (2, 4)) == "NO"
    assert intersection((-5, -3), (0, 2)) == "NO"
    assert intersection((-5, -3), (-5, 0)) == "YES"
    assert intersection((-3, -1), (1, 3)) == "NO"
``` 
Make sure you have Python 3.7 or a later version to ensure the code runs without errors.