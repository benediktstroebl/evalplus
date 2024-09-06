```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive function offers a straightforward approach to finding the greatest common divisor (GCD) of two integers a and b, following the Euclidean algorithm. It exploits the property that the GCD of two numbers equals the lesser of the two, if the larger number is divided by the smaller number without a remainder.

Should b be zero, indicating that a is the larger number, the function returns a directly. Otherwise, it recursively calls itself, substituting b with the remainder of a divided by b. With each recursive call, the divisor becomes increasingly smaller, leading to the GCD when the remainder becomes zero.

This algorithm is efficient, with a time complexity of O(log(min(a, b))). It's a concise and direct method to find the GCD.