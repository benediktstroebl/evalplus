### Modulus Power Function
Here is a self-contained Python script that implements the modulus power function `modp`.

```markdown
### Code
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    :param n: The exponent (base: 2)
    :param p: The modulus
    :return: 2^n modulo p
    """
    result = 1  # Initialize result to 1
    base = 2  # Base is 2
    
    # Use exponentiation by squaring for efficient computation
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p  # Multiply result by base and take modulus
        base = (base * base) % p  # Square base and take modulus
        n = n // 2  # Divide n by 2
    
    return result  # Return the final result

### Example Use Cases
if __name__ == "__main__":
    print(modp(3, 5))  # Output: 3
    print(modp(1101, 101))  # Output: 2
    print(modp(0, 101))  # Output: 1
    print(modp(3, 11))  # Output: 8
    print(modp(100, 101))  # Output: 1
```

### Explanation
The script defines a function `modp` that calculates the modulus power of 2 raised to a given exponent `n` with a modulus `p`. It uses the exponentiation by squaring technique for efficient computation. The function initializes the result to 1 and the base to 2. It then enters a while loop that continues until `n` is 0. Inside the loop, it checks if `n` is odd, and if so, it multiplies the result by the base and takes the modulus. It then squares the base and takes the modulus. Finally, it divides `n` by 2. The function returns the final result.

The script includes example use cases to demonstrate the function's behavior.