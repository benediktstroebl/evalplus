```python
def is_prime(n):
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
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > en:
        return "NO"
    elif is_prime(st - en + 1):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple algorithm to determine if the intersection's length is prime. The function `is_prime` checks if a given number `n` is prime or not. The function employs several optimization techniques to speed up the process by checking divisibility by 2 and 3, and then checking only the odd numbers for primality thereafter. 

The `intersection` function first calculates the start and end values, and then checks if the intersection is empty or not. If the intersection is not empty and the length of the intersection is prime, it returns "YES". Otherwise, it returns "NO". 

A few test cases are provided to validate the function. You can add more tests to cover more edge cases. 
```python -xv
import unittest

class Test(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_second_example(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_third_example(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_empty_intersection(self):
        self.assertEqual(intersection((10, 20), (30, 40)), "NO")
```

You can add more tests to cover other scenarios and edge cases.