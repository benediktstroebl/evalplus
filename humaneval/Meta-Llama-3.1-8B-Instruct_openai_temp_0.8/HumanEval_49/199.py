**Modular Power Function**
==========================

Here's a Python script that calculates 2^n modulo p efficiently using the binary exponentiation method:

```markdown
### modp.py

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    This function uses binary exponentiation to efficiently compute the result.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    result = 1
    base = 2

    # Use binary exponentiation to calculate 2^n
    while n > 0:
        # If the current bit is 1, multiply the result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and move to the next bit
        base = (base * base) % p
        # Move to the next bit in the exponent
        n = n // 2

    return result

if __name__ == "__main__":
    # Test cases
    print(modp(3, 5))    # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))  # 1
    print(modp(3, 11))  # 8
    print(modp(100, 101))  # 1
```

**Example Use Cases**
---------------------

This script defines a `modp` function that takes two arguments: `n` (the exponent) and `p` (the modulus). It uses binary exponentiation to efficiently calculate 2^n modulo p.

To use this function, simply call it with the desired values of `n` and `p`. The result will be printed to the console.

Note that this script includes test cases to demonstrate its correctness. These test cases cover a variety of inputs, including cases where n is large and p is small.

**Commit Message**
-----------------

`Added modp.py script to calculate 2^n modulo p using binary exponentiation`