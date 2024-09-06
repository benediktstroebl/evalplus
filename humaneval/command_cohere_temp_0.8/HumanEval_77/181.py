```python
def iscube(a):
    # Check if the number is divisible by 2 but not equal to 2
    if a % 2 != 0 and a != 2:
        return False

    # Check if the number is divisible by 3 but not equal to 0
    if a % 3 == 0 and a != 0:
        return False

    # Check special cases for 7, 8, 27
    if a == 1:
        return True
    if a == 7 or a == 8 or a == 27:
        return False

    # Check all divisors from 3 to the square root of N
    sqrt_a = int(a**0.5)
    for i in range(3, sqrt_a + 1, 2):
        if a % i == 0:
            if iscube(a // i) == True:
                return True

    return False
```

The approach uses a recursive method to check for divisors from 3 to the square root of the number, and returns True if any of them lead to a cube number when divided. It checks for special cases of 1, 7, 8, and 27, and also checks if the number is even but not equal to 2, or divisible by 3 but not equal to 0.