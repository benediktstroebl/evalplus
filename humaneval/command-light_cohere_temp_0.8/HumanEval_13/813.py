```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of inputs must be a positive integer.")

    if not (a % b == 0) or (b % a == 0):
        return a
    elif a == b:
        return a
    else:
        return 2  # Handle cases where a and b are relatively prime, e. fact greatest common divisor is largest number that divides both a and b evenly.  # O(lognitude) would be this number, but since we don't know the exact lcm, we return the maximum value that satisfies this condition.