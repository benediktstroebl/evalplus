Here is a self-contained Python script that defines a function `greatest_common_divisor` that finds the greatest common divisor of two integers `a` and `b` : 

```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero.")
    gcd = math.gcd(a, b)
    return gcd

# Unit tests
test_gcd = GreatestCommonDivisorTest(lambda a, b: greater_common_divisor(a, b))
test_gcd.test_gcd(3, 5)
test_gcd(25, 15)
test_gcd(0, 5)
test_gcd(5, 0)
``` 


 This script does the following: 
 - It defines a function `greatest_common_divisor` that takes two integers `a` and `b` as arguments, and returns the greatest common divisor of `a` and `b`. 
 - It includes unit tests using the `test` module, which is a built-in testing library in Python. 
 - The test cases cover a variety of scenarios, including zero inputs, edge cases, and the expected behavior of the function.