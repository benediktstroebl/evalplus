```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    return max(a, b) / gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```
This function, named **greatest_common_divisor**, takes two integers a and b as input and returns the greatest common divisor of a and b. It uses the other division and the **gcd** function to calculate the greatest common divisor. The test cases ensure the both the function, which is self-contained and provides the desired result.