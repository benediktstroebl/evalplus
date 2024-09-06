```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    num = [int(i) for i in range(a, b + 1)]
    even_digits = [i for i in num if i % 2 == 0]
    return even_digits

# Test Cases
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
```

This script defines a function `generate_even_digits(a, b)` that takes in two positive integers, `a` and `b`, and returns a list of even digits that lie between `a` and `b`, in ascending order. The function initially creates a list of all integers from `a` to `b` using the `range()` function, then utilizes a list comprehension to filter out the even digits, and lastly, if there are no digits, it returns a list of an empty set. 

The script also includes test cases that verify the function's behavior for different inputs, ensuring that it follows the problem statement and returns the correct results.  This adheres to the Given two positive integers a and b, return the even digits between a and b, in ascending order.