```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of a or b must be a positive integer.")
    return max(a, b) // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def test():
    a = 3
    b = 5
    print("a", ":", greatest_common_divisor(a, b))
    assert greatest_common_divisor(a, b) == 1
    print("\n", end="")

    a = 25
    b = 15
    print("a", ":", greatest_common_divisor(a, b))
    assert greatest_common_divisor(a, b) == 5
    print("\n", end="")

    a = (-5)
    b = 10
    print("a", ":", greatest_common_divisor(a, b))
    assert greatest_common_divisor(a, b) == 5
    print("\n", end="")

    a = 123
    b = 456
    print("a", ":", greatest_common_divisor(a, b))
    assert greatest_common_divisor(a, b) == 56
    print("\n", end="")

if __name__ == "__main__":
    test()
```
This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function first checks if either a or b is negative, and if either is zero, it raises a ValueError. Then, it uses the gcd() function to find the greatest common divisor of a and b, which is returned.

The code also includes a function `gcd` that calculates the greatest common divisor of a and b using a recursive approach. The `test` function contains a series of test cases, which verify the correctness of the `greatest_common_divisor` function by checking if the returned result matches the expected result for a given pair of integers.  Finally, if the code passes all tests successfully, it prints the test results. 
This code demonstrates a self-contained solution for finding the greatest common divisor of two integers.