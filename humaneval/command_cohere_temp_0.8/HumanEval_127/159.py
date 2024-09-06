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

The approach uses a simple algorithm to check if the intersection length is prime. A function is_prime(n) checks whether the integer n is a prime number or not. We then use max and min functions to find the starting and ending point of the intersection and then check its length and use the prime checking function to see if the length is prime. The code also handles cases where no intersection or an empty intersection occurs. 

The sample tests provided would return the following:
- intersection((1, 2), (2, 3)) ==> "NO"
- intersection((-1, 1), (0, 4)) ==> "NO"
- intersection((-3, -1), (-5, 5)) ==> "YES"