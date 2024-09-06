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

The approach uses a simple algorithm to determine if a number is prime or not. The algorithm checks if the number is less than or equal to 1, which it is not. Then, it checks if the number is divisible by 2 or 3, and it is not, so the algorithm continues. It then starts checking through numbers of the form 6k + (-)1, 6k + 1, 6k + 5 (these are primes when k is not divisible by 2 or 3) up to the square root of the number n, roughly speaking. If the square root is reached and the number hasn't been divisible by any number in the sequence, it's prime. Otherwise, it's not. 

The function `intersection` takes two intervals as input and returns "YES" if the length of the intersection is a prime number, and "NO" otherwise. The function first computes the start and end of the intersection of the two intervals using max and min functions respectively. It then checks if the end is greater than the start to return "NO" if they don't intersect. It then checks if the length of the intersection is a prime number by calling the `is_prime` function on the length and returns "YES" if true and "NO" otherwise.

The total time complexity of the provided code is O(sqrt(min(a[1] - a[0] + 1, b[1] - b[0] + 1))). This is because the algorithm used to check for prime numbers in the `is_prime` function runs up to the square root of the number being checked. The linear factor of the square root is present because the algorithm checks up to the square root of the number, and this is the best possible result one could achieve in polynomial time for this problem.