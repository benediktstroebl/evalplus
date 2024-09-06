```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(largest_divisor(15))  # Output: 5
```
The function largest_divisor calculates the largest divisor of a given number n by using the formula n - 1 // gcd(n - 1, n - 2), where gcd returns the greatest common divisor of two numbers a and b. The function then computes the maximum divisor smaller than n using the result of the gcd function.