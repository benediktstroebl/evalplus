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
    else:
        return "YES" if is_prime(st - s1[0] + 1 + en - s2[1] + 1) else "NO"

# Test cases
tests = [
    (intersection((1, 2), (2, 3)), "NO"),
    (intersection((-1, 1), (0, 4)), "NO"),
    (intersection((-3, -1), (-5, 5)), "YES"),
]

for case, expected in tests:
    assert case == expected
```

The approach involves the following steps:
1. **Intersection and Pruning**: Max of start values and min of end values of the two intervals gives the start and end of the intersection. If this interval is length 1 (coinciding start and end values), it is automatically not prime, avoiding the need to check this case. Additionally, if the intersection is empty, there is no intersection, and the function returns 'NO'.
2. **Prime Checking**: The length of the intersection is a prime number if and only if the difference between the end and start values of the original intervals (inclusive) is a prime number. This is because we are dealing with closed intervals, and the original definition of prime for integers mentions that a number is prime if it is divisible only by 1 and itself.

The above approach has a time complexity of `O(1)`, making it extremely efficient for this problem, as we only perform addition, subtraction, and primality checks that iterate only once over the intersection length.