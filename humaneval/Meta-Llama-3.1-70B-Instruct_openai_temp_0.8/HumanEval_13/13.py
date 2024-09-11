```python
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b

    This function uses the Euclidean algorithm to find the GCD.
    
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b!= 0:
        # Swap the values of a and b
        a, b = b, a % b
    return abs(a)

# Test cases
print(greatest_common_divisor(3, 5))   # Expected output: 1
print(greatest_common_divisor(25, 15)) # Expected output: 5
```
This Python script defines a function `greatest_common_divisor(a, b)` that takes two integers as input and returns their greatest common divisor (GCD) using the Euclidean algorithm. It includes two test cases to verify the correctness of the function.

**How it works:**

1. The function takes two integers `a` and `b` as input.
2. It enters a while loop that continues until `b` is zero.
3. Inside the loop, it swaps the values of `a` and `b`, and then updates `b` to be the remainder of `a` divided by `b` (`a % b`).
4. Once `b` is zero, the function returns the absolute value of `a`, which is the GCD of the original `a` and `b`.

**Example use cases:**

* Finding the GCD of two numbers to simplify fractions or reduce the size of images.
* Computing the least common multiple (LCM) of two numbers, which is equal to the product of the numbers divided by their GCD.
* Solving Diophantine equations, which involve finding integer solutions to linear equations.