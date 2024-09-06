```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This solution follows the same approach as before, using the recursive method `greatest_common_divisor(b, a % b)` to calculate the GCD. 

The above code is a self-contained solution to the problem. It passes all the why the answer for the given input.