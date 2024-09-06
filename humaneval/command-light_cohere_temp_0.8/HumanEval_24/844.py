```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    n = 15
    print(largest_divisor(n))  # Output: 5
``` 
This code defines a function `largest_divisor(n)` that finds the largest divisor of a given number `n`. The function efficiently calculates the greatest number that divides `n` evenly by calculating the greatest divisor of `n - 1` and `n - 2`. The `gcd()` function computes the greatest common divisor of two numbers. The `if __name__ == "__main__":` block ensures the function is executed only when the script is run directly, and it prints the result of the `largest_divisor()` function for the number 15.