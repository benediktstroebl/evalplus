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
    s = max(s1[0], s2[0]) - min(s1[0], s2[0]) + 1
    if s1[1] < s2[1]:
        s = max(s, s1[1] - s2[0]) + 1
    elif s2[1] < s1[1]:
        s = max(s, s2[1] - s1[0]) + 1
    else:
        s = max(s1[1] - s2[0], s2[1] - s1[0]) + 1
    if is_prime(s):
        return "YES"
    else:
        return "NO"

# Test cases
tests = [
    ((1, 2), (2, 3), "NO"),
    ((-1, 1), (0, 4), "NO"),
    ((-3, -1), (-5, 5), "YES"),
]

for s1, s2, answer in tests:
    result = intersection(s1, s2)
    if result != answer:
        print(f"Error on test case: {s1}, {s2}, expected: {answer}, actual: {result}")
```

The code above includes a `is_prime` function that checks if a given number is prime or not. The `intersection` function calculates the length of the intersection of two intervals and then checks if the length of the intersection is a prime number or not. The `tests` list contains test cases that can be used to verify the correctness of the `intersection` function. 

You can add this test suite to your Python code to validate the correctness of the `intersection` function, and accordingly adjust the code if needed. Feel free to modify the tests according to the cases you might have in mind to further ensure the correctness of the function.