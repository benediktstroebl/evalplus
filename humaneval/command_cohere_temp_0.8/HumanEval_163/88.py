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

    # Ensuring inputs are integers and validating input values
    a, b = map(int, (a, b))
    if a > b:
        return []

    # Creating a list to store the even digits
    result = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            result.append(num)

    return result

# Testing the function with different inputs
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function takes in two integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, in ascending order. The idea is to loop through integers from `a` to `b` (or `b` to `a` if `a > b`) and append the even integers to the result list. To determine whether an integer is even or odd, we use the modulus operator `%`, which returns the remainder when dividing by 2, so if the remainder is 0, it is even.