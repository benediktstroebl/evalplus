Here's a self-contained Python function that finds the GCD of two integers using the Euclidean algorithm: 

```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)

# test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 

The script has a function that recursively computes the GCD of two integers a and b. The function terminates when a and returns b if a is 0, otherwise it returns the result of calling greatest_common_divisor(b%a, a), which is the GCD of b and a. appearance on the Euclidean algorithm, which has a time complexity of O(log(min(a, b))) according to the Big O notation.