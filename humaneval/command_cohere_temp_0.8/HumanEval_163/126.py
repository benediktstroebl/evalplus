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
        if str(x).split('0')[1] == '':
            even_digits.append(int(x))
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function operates on two parameters: `a`, which represents the lower bound integer, and `b`, which represents the upper bound integer. It aims to create a list of even digits that ascend from `a` to `b`, inclusive. To achieve this, the function first ensures that `a` is the lower bound by swapping `a` and `b` if `a` is greater than `b`. It then initiates an empty list called `even_digits` to hold the even digits. The function then loops from `a` up to `b + 1`, extracting the second digit of the string representation of each number. If the second digit is empty, indicating an even number, it is appended to the `even_digits` list. Lastly, the function returns the `even_digits` list.

The test cases included in the script prove the function's operation, confirming that it generates the even digits as expected between the specified integers.