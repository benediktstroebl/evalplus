Here is a self-contained Python script that defines a function `greatest_common_divisor` that finds the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    return max(a, b) / math.gcd(a, b)

# Unit tests
test_gcd = GreatestCommonDivisorTestCase(gcd=math.gcd)
test_gcd(3, 5)=1
test_gcd(25, 15)=5
``` 
This function uses the `math.gcd` function to calculate the greatest common divisor using the Euclidean algorithm.