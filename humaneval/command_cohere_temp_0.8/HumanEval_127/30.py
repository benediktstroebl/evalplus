```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    st, ed = max(s1[0], s2[0]), min(s1[1], s2[1])
    if ed - st + 1 < 2:
        return "NO"
    elif is_prime(ed - st + 1):
        return "YES"
    else:
        return "NO"

# Example usage
print(intersection((1, 2), (2, 3))) == "NO"
print(intersection((-1, 1), (0, 4))) == "NO"
print(intersection((-3, -1), (-5, 5)) == "YES")
```

The `is_prime` function is used to determine if a given number is prime. This function checks if the number is less than 2, or if it has any divisors between 2 and the square root of the number. If any divisors are found, or if the number is less than 2, it returns `False`; otherwise, it returns `True`. 

The `intersection` function calculates the intersection of two intervals, assuming they are closed intervals. It returns "NO" if the intersection has a length less than 2 or if it is not prime. Otherwise, it returns "YES" if the intersection length is prime. 

The example usage demonstrates how the `intersection` function can be used to solve the problem statement provided.