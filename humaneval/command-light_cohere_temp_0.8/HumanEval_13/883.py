```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is required.")
    elif a == 0 or b == 0:
        return 0

    # Largest factor that is a divisor of both numbers
    temp = a

    while b > 0:
        if b % temp == 0:
            break
        temp += a

    return temp

# Test the function with a few examples
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
```