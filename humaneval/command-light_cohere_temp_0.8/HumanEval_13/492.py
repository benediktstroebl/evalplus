```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    else:
        return max(a, b) // gcd(a, b)
 
# unit tests
test_gcd = {}
test_gcd[0] = (1, 0)
test_gcd[1] = (1, 1)
test_gcd[2] = (2, 0)
test_gcd[3] = (3, 3)
test_gcd[4] = (4, 2)
test_gcd[5] = (5, 5)
test_gcd[6] = (6, 0)
test_gcd[7] = (7, 7)
test_gcd[8] = (8, 8)
test_gcd[9] = (9, 9)
test_gcd[10] = (10, 10)

def test_gcd():
    for i, (a, b) in enumerate(test_gcd.items()):
        print("Test case", i + 1, ":", a, b)
    result = greatest_common_divisor(a, b)
    print("Result:", result)
test_gcd()
``` 
This Python code defines a function called `greatest_common_divisor` that calculates and returns the greatest common divisor of two integers `a` and `b`. The function uses the Euclidean algorithm along with the `gcd` function to find the greatest common divisor. The code also includes a unit tests, which cover a variety of test cases for the `greatest_common_divisor` function.