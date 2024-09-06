```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.isgcd(min(a, b))

def test_greatest_common_divisor():
    try:
        a = 3
        b = 5
        print(f"The greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)} = {1}")
    except ValueError as e:
        print(f"Error: {e}")
    return

# Test case 2
try:
    a = 25
    b = 15
    print(f"The greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)} = {5}")
except ValueError as e:
    print(f"Error: {e}")

# Test case 3
try:
    a = 2
    b = 3
    print(f"The greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)} = {1}")
except ValueError as e:
    print(f"Error: {e}")

# Test case 4
try:
    a = -2
    b = 3
    print(f"The greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)} = {1}")
except ValueError as e:
    print(f"Error: {e}")

test_greatest_common_divisor()
```