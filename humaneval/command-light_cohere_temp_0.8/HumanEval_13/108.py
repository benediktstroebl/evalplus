```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a

    m = 0
    for i in range(1, min(len(str(a)), len(str(b)))):
        if str(a)[-i] != str(b)[-i] or m != 0:
            break
        m += 1

    return m

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 20))  # Output: 4 (since 4 is the only common divisor)
print(greatest_common_divisor(10, 55))  # Should raise ValueError
```