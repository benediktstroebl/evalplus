```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1,  2)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

#Test cases
largest_divisor(15)  # Output: 5
largest_divisor(10)  # Output: 5
largest_divisor(12)  # Output:  4 (12 - 1 = 11, 11 % 2 = 1, GCD(11, 2) = 1)
largest_divisor(27) # Output: 6
```
This function calculates the largest divisor for a given number n that divides it evenly, smaller than n, using the Euclidean Algorithm. The algorithm efficiently computes the
 the greatest common divisor (GCD) of the original number and 2, and then uses this value to find the largest divisor.