```python
def is_prime(n):
    """
    Checks if a number is prime
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
    Check whether the intersection of two intervals is prime
    """
    if s1[0] > s2[1] or s1[1] < s2[0]:
        return "NO"
    inter_start = max(s1[0], s2[0])
    inter_end = min(s1[1], s2[1])
    if is_prime(inter_end - inter_start):
        return "YES"
    else:
        return "NO"
```
The aforementioned function utilizes a prime checking function, `is_prime`, to determine whether the intersection of two intervals is prime. A brief explanation of `is_prime` is provided below:
1. The function initially determines whether the given number is less than or equal to 1, in which case it inevitably returns False.
2. It then checks whether the number is equal to 2 or 3, thereby confirming its primality and subsequently returning True.
3. The function verifies whether the number is divisible by 2 or 3, subsequently terminating the process and returning False.
4. The function enters a loop where it commences with the value i = 5. This loop iterates through numbers incremented by 6 (i.e., 5, 11, 17, 23, 29, etc.) until the square of i becomes less than or equal to the given number.
5. Within the loop, the function checks whether the given number is divisible by i or i + 2. If it is, the function returns False.
6. If the loop exhausts all viable candidates for divisors, the function returns True.

The `intersection` function incorporates the `is_prime` function to determine whether the length of the intersection of two intervals is prime. To facilitate this process, the function ascertains the starting point and duration of the intersection. Subsequently, it employs `is_prime` to evaluate whether the duration (difference between the end and start) is prime. If it is, the function returns "YES". If the duration is not prime, it returns "NO". Moreover, the function cross-checks the intervals to ascertain whether they actually intersect, and if they don't, it also returns "NO".