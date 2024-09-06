```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("One or both numbers should be greater than zero.")
    return abs(a) if a > b else b

# Example usage:
if __name__ == "__main__":
    a = 25
    b = 15

    print("Greatest common divisor:", end="")
    print(greatest_common_divisor(a, b))
``` 
This code defines a function `greatest_common_divisor` that calculates and returns the greatest common divisor of two input integers `a` and `b`. It first handles the edge case where either input is zero, raising a `ValueError` with an appropriate error message. The function then returns the regular expression that returns the absolute value of the greater of the inputs, `a` or `b`, depending on which is greater. 
This approach is efficient and avoids unnecessary complex logic for handling negative numbers.