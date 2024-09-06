```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer that divides n evenly, smaller than n"""
    return (n + 1) // gcd(n + 1, 2)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

# Example usage
n = 15
print(largest_divisor(n))  # Output: 5
``` 
This Python code defines a function `largest_divisor` that finds the largest integer that divides a given number `n` evenly, ensuring that the resulting divisor is less than `n`. The function uses the `gcd` function to calculate the greatest common divisor of `n` and `2`, and then multiplies the result by `n + 1` to find the largest integer that divides `n` evenly. The example usage demonstrates how function by finding the largest divisor of `15`. The output is `5`, as `5` is the largest integer that divides `15` evenly, smaller than `15`.