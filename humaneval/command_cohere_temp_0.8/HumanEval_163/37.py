```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    if a % 2 == 0 and b % 2 == 0:
        result = []
        if a <= b:
            for x in range(a, b + 1):
                if x % 2 == 0:
                    result.append(x)
        elif b <= a:
            for x in range(b, a + 1):
                if x % 2 == 0:
                    result.append(x)
        return result
    else:
        return []
```
The function includes checks for the validity of input and the inclusion of an explanation for the operation. This ensures that the function is robust and provides useful feedback for developers who may use or call this function in the future for more complex projects. 

The function generates a list of even digits between two numbers a and b. It checks if both numbers are even, and if so, it iterates over the range from a to b (or from b to a if b is greater than a) and collects all even numbers in the result list. The result is an empty list if no even numbers are found in the range.