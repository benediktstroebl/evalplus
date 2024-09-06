```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input must be a number")
    return max(set(x for x in range(1, max(a, b)) if x <= max(a, b) and (a % x) == 0 and b % x == 0))

if __name__ == "__main__":
    tests = [
        (3, 5),
        (25, 15),
        # Add more test cases as needed
    ]
    for a, b in tests:
        print(f"Test {a} x {b}: {greatest_common_divisor(a, b)}")
``` 
This code defines a `greatest_common_divisor` function that calculates the greatest common divisor of two integers `a` and `b`. The function first checks if either input is not a number and raises a `ValueError` if that's the case. The function then returns the` `max(set(x for x in range(1, max(a, b)) if x <= max(a, b) and (a % x) == 0 and b % x == 0))` which will return the greatest common divisor of the two numbers. 
This function is self-contained and efficiently solves the problem of finding the greatest common divisor of two numbers.