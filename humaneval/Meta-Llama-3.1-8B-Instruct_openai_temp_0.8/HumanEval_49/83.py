### Exponentiation Modulo p
#### Problem
The problem asks to implement a function `modp(n: int, p: int)` that calculates the result of 2^n modulo p.

#### Solution
```python
def power_mod(base: int, exponent: int, modulo: int) -> int:
    """
    Compute (base ^ exponent) % modulo efficiently using binary exponentiation.

    Args:
        base (int): The base number.
        exponent (int): The exponent to which the base is raised.
        modulo (int): The modulo value.

    Returns:
        int: The result of (base ^ exponent) % modulo.
    """
    result = 1
    base = base % modulo
    while exponent > 0:
        # If the exponent is odd, multiply the result by the current base
        if exponent % 2 == 1:
            result = (result * base) % modulo
        # Square the base and divide the exponent by 2
        base = (base * base) % modulo
        exponent = exponent // 2
    return result


def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Args:
        n (int): The exponent.
        p (int): The modulo value.

    Returns:
        int: The result of 2^n modulo p.
    """
    return power_mod(2, n, p)


# Example use cases
if __name__ == "__main__":
    print(modp(3, 5))    # Output: 3
    print(modp(1101, 101))  # Output: 2
    print(modp(0, 101))  # Output: 1
    print(modp(3, 11))  # Output: 8
    print(modp(100, 101))  # Output: 1
```
This code defines two functions: `power_mod` for computing the power modulo operation using binary exponentiation, and `modp` for computing 2^n modulo p. The `power_mod` function uses a while loop to iterate through the bits of the exponent, squaring the base when the exponent is even and multiplying the result by the base when the exponent is odd. The `modp` function simply calls `power_mod` with a base of 2.