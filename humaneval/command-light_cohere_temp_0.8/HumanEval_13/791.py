```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid")
    return max(divisor(a) ,divisor(b))

def divisor(x):
    if not x:
        raise ValueError("Input cannot be zero")
    return [i for i,d in enumerate(x) if not d or d==1]

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
```
The function `greatest_common_divisor` calculates the greatest common divisor of two integers a and b using the divisor helper function.  The maximum of these smallest common divisor of a and b, or raise an error if either input is invalid (zero or not a number).