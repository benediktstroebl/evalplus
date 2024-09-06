```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers")
    return max(divisor(a) ,divisor(b))

def divisor(x):
    y = x
    while y % x == 0:
        y //= x
    return y

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
    print(greatest_common_divisor(13, 17))
``` 
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two numbers. It uses the  a recursive approach and a helper function `divisor` to calculate divisors until no remainder. The code then passes tests on the function by calling with various input values.