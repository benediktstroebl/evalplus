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
        s = max(s, s1[1] - s2[0] + 1)
    elif s2[1] < s1[1]:
        s = max(s, s2[1] - s1[0] + 1)
    if s == 1:
        return "NO"
    if is_prime(s):
        return "YES"
    else:
        return "NO"
```

The approach uses a simple optimization by checking the intervals separately first before computing the intersection length. We also use a optimized primality testing function for comparing the length. 
The `is_prime` function uses trial division with small primes to quickly determine primality. 

The `intersection` function first calculates the intersection length with a check to ensure the resulting length is more than 1, if so, it proceeds to check if the length is prime using our primality testing function. 

This solution has a time complexity of `O(max(a, b) + abs(a - b) + max(a, b) * log(max(a, b)))` and uses trial division which has a worst-case time complexity of `O(sqrt(n))` for the primality test. 

Note that the code block provided earlier has a small typo, the `s1[1] < s2[1]` condition should be swapped in the else branch for accuracy. This correction has been made in the provided Python script above.