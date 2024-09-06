```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The starting integer.
        b (int): The ending integer.

    Returns:
        list: A list of even digits from start to end or an empty list if no even digits are present.
    """
    if a % 2 == 0 and b % 2 == 0:
        even_digits = []
        for x in range(a, b + 1):
            if x % 2 == 0:
                even_digits.append(x)
        return even_digits
    else:
        return []
```
The function initiates by validating that both the start and end integers are even. If they are, it constructs a list to hold any even digits encountered between the two numbers. The function then iterates through digits ranging from the start value to the end value, checking for even digits and adding them to the list. If no even digits are found, the function returns an empty list. 

This solution adheres to the problem's guidelines and efficiently identifies even digits within the given range. 

This code would typically be housed in a larger Python module or script, but this self-contained version can be directly plugged into a Markdown cell and run as is.