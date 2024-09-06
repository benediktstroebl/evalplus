Here's a self-contained Python script that defines a function `greatest_common_divisor` solving the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")
    elif a == b:
        return a
    else:
        gcd = []
        while a != 0:
            gcd.append(b % a prev)
            a = b
            b = gcd[-1]
        return max(gcd)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```

This script defines a function that calculates the greatest common divisor of two integers a and b. The function first checks if either of the inputs is zero, and if so, raises a `ValueError`. If both inputs are not zero, it checks if a and b are equal and returns a, otherwise, it uses the Euclidean algorithm to find gcd. The function returns the maximum of the list of remainders when appended to b until a is zero.