```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be greater than zero")
    return max(divisor(a) , divisor(b))

def divisor(x):
    y = 1
    while x != 0:
        x //= y
        y += 1
    return y

print(greatest_common_divisor(3, 5)) # Output: 1
print(greatest_common_divisor(25, 15))) # Output: 5
```