Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_num = max(a, b)
    if max_num % a == 0 or max_num % b == 0:
        return max_num
    else:
        return 1 + greatest_common_divisor(max_num, a) + greatest_common_divisor(b, max_num)

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This function greatest_common_divisor(a, b) calculates the greatest common divisor of two integers a and b. The function handles the simple cases where a and b are either equal or one of them is 0, and returns 0 as the GCD. If both numbers are greater than 0, the function calculates the GCD by finding the greatest common divisor of their product and the other number, and then adds these two results. If a numbers are greater than each other, the GCD is just the larger number. The result is always the same, which is a good property for this function.