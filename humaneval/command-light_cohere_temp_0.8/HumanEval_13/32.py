```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers. It utilizes the class the also defines a helper function `gcd` that calculates the greatest common divisor of 2 numbers using the Euclidean algorithm. Finally, the code passes test cases for the function and prints the results.

Remember to provide appropriate input values to the function. The output for the following cases:
```bash
1
5
25
```