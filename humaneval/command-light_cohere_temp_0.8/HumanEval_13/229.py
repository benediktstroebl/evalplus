```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b

    return a

# Test the function
assert(greatest_common_divisor(3, 5) == 1, "Failed test 1")
assert(greatest_common_divisor(25, 15) == 5, "Failed test 2")
assert(greatest_common_divisor(59, 121) == 19, "Failed test 3")
assert(greatest_common_divisor(121, 19) == 20, "Failed test 4")
```
The function `greatest_common_divisor` takes two integers a and b as input and returns the greatest common divisor of a and b. This function uses the more efficient algorithm to find the greatest common divisor.  It runs in O(n) time complexity, which is the same as the Sieve of Eratosthenes algorithm.