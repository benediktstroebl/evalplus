```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return greatest_common_divisor(b, a % b)  # Recursive call to find the greater divisor
```
This function greatest_common_divisor takes two integers a and b as input and returns the greatest common divisor of a and b. Recursively calling theild the need to pass the following tests:
1. Minimum input of zero.
2. minimum input isinput must lead to an runtime error.

The function follows these steps:
1. finding: If either a or b is 0, the function returns 0, indicating that there is no common divisor.
2. If b is 1, the function returns a, indicating that a is the greatest common divisor.
3. Otherwise, the function recursively calls itself with the parameters b and a% b to find the greater divisor. 

Please note that you can run this script to test the `greatest_common_divisor` function, and it should provide the expected output for the given inputs.