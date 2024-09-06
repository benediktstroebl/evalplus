```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient and is based on the Euclidean algorithm that always finds the GCD of two integers a and b in finite time. This algorithm repeats the process until 'b' becomes 0. Each iteration finds the remainder which is common between a and b, and the divisor b updates to this common remainder. When b becomes 0, the result is the remainder, which is the GCD of the given integers 'a' and 'b'. 
This approach does not require any imports. It is self-contained and efficient in solving the given problem. It's also worth noting that the Euclidean algorithm is directly built into the built-in `math.gcd` function in Python, so if you prefer a more straightforward approach, you can use that. Here's a brief explanation: 
```python
import math

def greatest_common_divisor(a, b):
    return math.gcd(a, b)
```
This approach uses a built-in function, so it is both efficient and self-contained. Let me know if this solution works for you, and if you have any further questions or feedback, feel free to ask!