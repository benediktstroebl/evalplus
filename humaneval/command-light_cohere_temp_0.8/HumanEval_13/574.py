```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_div = 0
    for i in range(1, min(int(a ** 0.5),5, b ** 0.25):
       
       
        while i <= max_div:
            if a % i == 0 and b % i == 0:
                max_div = i
                break

    return max_div

# Test cases go here:
print(greatest_common_divisor(3, 5)) # Output: 1
print(greatest_common_divisor(25, 15)) # Output: 5
print(greatest_common_divisor(12, 47)) # Output: 17
```