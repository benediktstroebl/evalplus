Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n"""
    res = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            res.append(i)
    return res

# Tests
test_cases = [
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (0, []),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (1, []),
    (18, [2, 3, 5, 7, 11, 13, 17])
]

for case in test_cases:
    assert count_up_to(case[0]) == case[1]
```
This script includes a 'is_prime' function that correctly determines whether or not an integer is prime, and a 'count_up_to' function that utilizes the 'is_prime' function to solve the problem. Both functions are included in the same code snippet as per your specifications. Also, the script includes a few test cases to verify the correctness of the implemented solution. You can use these test cases as a starting point and add more to ensure the function is correct and robust for all cases.