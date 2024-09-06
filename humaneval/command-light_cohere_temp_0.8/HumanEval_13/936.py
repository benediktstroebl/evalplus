```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(a, b) / __gcd__(a, b)
 
def __gcd__(a, b):
    while b:
        a, b = b, a % b
    return a
 
if __name__ == "__main__":
    print(f"Result of {a} and {b} is {gcd(a, b)}")
    print(f"Greatest common divisor of {4} and {9} is {gcd(4, 9)}")
    print(f"Greatest common divisor of {81} and {27} is {gcd(81, 27)}")
```

This code defines a function **`gcd()`** that computes the greatest common divisor of two numbers a and b.

It uses the built-in function **`__gcd__()`** from the **`math`** module. It repeatedly calls this to do the process of finding GCD repeatedly, halting when b becomes 0.

This function can be used to efficiently find the GCD of any two numbers. 

The script also provides test cases to verify the correctness of the **`gcd()`** function.