```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a

    while a != 0:
        a, b = divmod(a, b)
        if a == 0:
            break

    return b

# Test case 1
assert greatest_common_divisor(3, 5) == 1

# Test case 2
assert greatest_common_divisor(25, 15) == 5

# Test case 3
assert greatest_common_divisor(27, 18) == 9

# Test case 4
assert greatest_common_divisor(9, 27) == 3

# Test case 5
try:
    greatest_common_divisor(-3, 4)
except AssertionError as e:
    print(f"Error: {e}")
```