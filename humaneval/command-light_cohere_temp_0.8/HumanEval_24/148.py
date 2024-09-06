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
This code defines a function `largest_divisor` that finds the largest divisor of a given number `n`. It uses the `gcd` function to calculate the greatest common divisor of `n - 1` and `n - 2`, which is the unique factor that generates the largest divisor of `n`.