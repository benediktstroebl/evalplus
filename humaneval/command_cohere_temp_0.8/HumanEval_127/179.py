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
    elif is_prime(st - s1[0] + s2[0]) and is_prime(en - st + s1[1] - s2[1]):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple algorithm to determine if a number is prime or not. The function `is_prime` determines if a given number n is prime or not. The function `intersection` determines if the length of the intersection of two intervals is prime. To do this, we find the maximum and minimum values of the starting points and ending points of both intervals. Then, we check whether the range of intersection is prime using the `is_prime` function. We also check during the evaluation of the function that the start of the interval is less than the end of the interval. This is done to ensure that we are dealing with a valid interval and to prevent any error. The approach is straightforward and simple to implement as it only requires the definition of a function to check if a number is prime or not, and uses some logic to find the prime of the intersection of two intervals.