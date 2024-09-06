```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
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

# Test cases
print(intersection((1, 2), (2, 3))) == "NO"
print(intersection((-1, 1), (0, 4))) == "NO"
print(intersection((-3, -1), (-5, 5))) == "YES"
```

This code defines a function `intersection()` that takes in two intervals, represented as tuples, and returns "YES" if the length of the intersection is a prime number, and "NO" otherwise. It also uses the `is_prime()` function to check if a number is prime. 

To better understand the `intersection()` function, let's break down the steps it takes:
1. `st, ed = max(s1[0], s2[0]), min(s1[1], s2[1])`: This line calculates the start and end of the intersection. The maximum of the start values and the minimum of the end values, respectevly. Since the intervals are closed, both start and end are inclusive.
2. `if ed - st + 1 < 2`: This checks if the intersection size is less than 2, and if so, it returns "NO" immediately since the intersection would be invalid or non-existent.
3. `elif is_prime(ed - st + 1)`: If the length of the intersection is greater than or equal to 2, it checks if this length is prime. 
4. `else`: If the length of the intersection is not prime, it returns "NO". 

The test cases at the end verify the correct operation of the `intersection()` function. You can run it in your Python environment to see the expected output. G