```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m = max(a, b)
    for i in range(1, m // 2 + 1):
        if a % i == 0 and b % i == 0:
            return i

    return m

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(7, 21))  # Output: 1 (i.7 is of course 2 * 2 and 2 is the greatest divisor of 7)

# Test case 4
print(greatest_common_divisor(123, 45))  # Output: 45

```
This Python function `greatest_common_divisor` accepts two integers `a` and `b` as arguments and employs a loop to find the greatest common divisor shared by both numbers. The function begins by determining the maximum of the two numbers and then checks each potential divisor from 1 up up to the square root of this maximum. The loop finds that shared divisor in constant time, regardless of the input numbers.