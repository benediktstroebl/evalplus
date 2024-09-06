```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    """
    Determine whether the length of intersection of two given closed intervals is a prime number.
    """
    # Convert interval to python interval
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    if end - start <= 1:
        return "NO"
    else:
        return "YES" if is_prime(end - start) else "NO"
```

The method 'is_prime' is included in this code to determine whether a given number is prime or not. It checks if the number is less than or equal to one, and if so, it returns 'False'. It also checks for the number's divisibility by any integer between 2 and the square root of the number, and if so, it returns 'False'. If neither of these conditions are met, the function returns 'True'.

A sample test that can be used to validate the functionality of the function is as follows:
```python
test = [
    (intersection((-3, -1), (-5, 5)), "YES"),
    (intersection((-1, 1), (0, 4)), "NO"),
    (intersection((1, 2), (2, 3)), "NO"),
]
``` 

The expected output would then be:
```python
['YES', 'NO', 'NO']
``` 

This would confirm the expected output for the test cases, highlighting how the function can successfully determine if the length of the intersection of two intervals is a prime number or not. 

This code can be run directly to test out the functionality of the `intersection` function and see if the outputs are as expected.