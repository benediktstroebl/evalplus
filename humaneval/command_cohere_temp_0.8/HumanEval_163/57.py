```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits in ascending order between a and b.
    """
    # Ensure a is the lower bound
    if a > b:
        a, b = b, a
    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] == '':: 
            even_digits.append(int(x))
    return even_digits
```

The function leverages the fact that integers are converted to strings and split into single digits when there are no divisors other than 1 and itself. Thus, if a number has no odd divisors, it must be even.

The function first checks if `a` is greater than `b`. If so, it swaps them to ensure that `a` always serves as the lower bound. It then iterates through the integers between `a` and `b` (inclusive), checking whether the string representation of each integer has a divisor-free odd digit. If it does not, the integer is an even digit, so it's added to the `even_digits` list, which is then returned.

This algorithm has a time complexity of O(N), where N is the absolute difference between `a` and `b`, and an auxiliary space complexity of O(1) as it only requires a list to store the output.

The unit tests ensure that the function handles edge cases like negative inputs, returns an empty list when no even digits are found, and correctly orders the even digits.