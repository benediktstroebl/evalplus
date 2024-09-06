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
    # Convert the interval pair to a tuple of (start, end) format
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    
    # Check if there is an intersection
    if end < start:
        return "NO"
    
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"
```

The `is_prime` function checks if a number is prime. It loops from 2 to the square root of the number and checks for divisibility. If the number is divisible by any integer in that range it returns `False`. If the number is not divisible by any integer in that range it returns `True`. 

The `intersection` function takes two interval pairs using the format `(start, end)`. It calculates the start and end of the intersection of the two intervals, and then calculates the length of the intersection. If the length of the intersection is prime it returns `YES`, otherwise it returns `NO`. If the two intervals don't intersect, it returns `NO`. 

You can use these functions in a `main` function, or `unittest` framework to test the functions with different inputs. Here is an example using the `unittest` framework:
```python
import unittest

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
    # Convert the interval pair to a tuple of (start, end) format
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    
    # Check if there is an intersection
    if end < start:
        return "NO"
    
    length = end - start + 1
    if is_prime(length):
        return "YES"
    else:
        return "NO"

class TestIntersection(unittest.TestCase):
    def test_intersection((1, 2), (2, 3)), (2, 3):
        """
        Test case where there is an intersection
        """
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_intersection((-1, 1), (0, 4)), (-1, 0):
        """
        Test case where there is an intersection
        """
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_intersection((-3, -1), (-5, 5)), (-4, -1):
        """
        Test case where there is an intersection
        """
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_intersection((1, 2), (2, 3)), ():
        """
        Test case where