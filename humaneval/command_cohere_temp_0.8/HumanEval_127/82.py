```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(s1, s2):
    st, en = max(s1[0], s2[0]), min(s1[1], s2[1])
    if en - st + 1 < 2:
        return "NO"
    elif is_prime(en - st + 1):
        return "YES"
    else:
        return "NO"

# Test cases
print(intersection((1, 2), (2, 3))) == "NO"
print(intersection((-1, 1), (0, 4))) == "NO"
print(intersection((-3, -1), (-5, 5)) == "YES")
```

This code defines a function `intersection()` that takes in two intervals, each represented as a tuple of two integers, and returns whether the length of the intersection of these two intervals is a prime number or not. 

The `is_prime()` function is also defined to determine whether a given integer is a prime number or not. It returns 'True' if the number is prime, and 'False' otherwise.

The `intersection()` function first checks if the end point is larger than the start point to verify if there is actually an intersection. It then calculates the length of the intersection and checks if this length is prime using the `is_prime()` function. If it is prime, it returns "YES"; otherwise, it returns "NO".

The test cases printed in the markdown code block are also included in the script to demonstrate how the `intersection()` function works.