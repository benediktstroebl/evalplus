```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero.")
    return max(divisor(a), divisor(b))

def divisor(x):
    y = 1
    while x != 0:
        x, y = divmod(x, 2)
        y += 1
    return y

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)} = {b}")
```