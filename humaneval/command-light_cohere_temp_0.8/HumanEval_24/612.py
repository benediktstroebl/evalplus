```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 2)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(largest_divisor(15))
``` 
The function largest_divisor calculates the largest number that evenly divides a given number n, smaller than or equal to the input. The gcd function calculates the largest integer that divides both numbers a and b evenly, then returns the result.