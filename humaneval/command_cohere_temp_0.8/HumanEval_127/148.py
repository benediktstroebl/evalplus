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
    st, ed = max(s1[0], s2[0]), min(s1[1], s2[1])
    if st > ed:
        return "NO"
    elif is_prime(st - ed + 1):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple algorithm to determine if a number is prime or not. The function `is_prime` checks if a given number n is less than or equal to 1, it returns False. If n is 2 or 3, it returns True. Then it checks whether n is divisible by 2 or 3, and if so, it returns False. For n > 3, it checks for divisibility by numbers of the form 6k ± 1 up to the square root of n. If the number is not divisible by 2, 3, or any number of the form 6k ± 1, it is a prime number, so True is returned. 

The function `intersection` maximizes the start value and minimizes the end value of both intervals. Then it checks if the length of the intersection is greater than 1, and if so, it checks if that length is a prime number, using the previously mentioned `is_prime` function. 

The total time complexity of the program is O(√n), where n is the length of the intersection. This is because the `is_prime` function iterates through numbers up to the square root of the length of the intersection.  In the worst-case scenario, every number will be checked, this happens when the intersection is [1,n], and n is greater than 2.  The space complexity is O(1) and it is always constant no matter the input. 

Note that this approach assumes that the start of an interval is inclusive and the end of an interval is not inclusive, which is consistent with the problem statement. 

To verify the correctness of the script, you can run the following test cases:
```python
test_cases = [
    ((1, 2), (2, 3), "NO"),
    ((-1, 1), (0, 4), "NO"),
    ((-3, -1), (-5, 5), "YES"),
    ((1, 3), (2, 4), "NO"),
    ((-5, 5), (-3, 3), "YES"),
    ((-10, -10), (0, 10), "NO"),
    ((-10, 10), (-10, 10), "YES"),
]

for s1, s2, expected in test_cases:
    actual = intersection(s1, s2)
    assert actual == expected, f"For inputs {s1} and {s2}, expected '{expected}' but got '{actual}'."
```

This problem can be solved in various ways, such as using pruning techniques or employing more efficient prime-checking algorithms like the Sieve of Eratosthenes. 

This code is not the most efficient approach for checking if a number is prime, especially for larger numbers. However, due to the size of the intersection and the constraints provided by the problem, using a more complex algorithm like the S