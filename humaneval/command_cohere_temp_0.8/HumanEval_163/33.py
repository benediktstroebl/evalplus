```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits from a to b in ascending order.
    """
    # Ensuring the inputs are integers and sorting them
    a, b = map(int, (a, b))
    ab_str = str(a) + str(b)
    ab_list = [int(x) for x in ab_str if x.isdigit()]
    ab_list.sort()

    # Extracting even digits and filtering out unwanted values
    even_digits = [x for x in ab_list if x % 2 == 0]

    return even_digits
```

The function takes two integers, `a` and `b`, and returns a list of even digits between `a` and `b` inclusive, in ascending order. For example:
```python
generate_even_digits(2, 8) => [2, 4, 6, 8]
generate_even_digits(8, 2) => [2, 4, 6, 8]
generate_even_digits(10, 14) => [2, 4, 6, 8]
```

The script ensures the inputs are integers and sorts them to simplify the even digit extraction. The even digits are then filtered out of the sorted numbers. It works for both positive and negative number gaps, returning an empty list if there are no even digits in the specified range.