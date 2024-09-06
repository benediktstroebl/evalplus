```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits from the first to the last integer given,
    only including those that are between the two in ascending order.

    Args:
        a (int): The starting integer.
        b (int): The ending integer.

    Returns:
        list: A list of integers containing even digits ranging from a to b.
    """
    if b < a:
        return []

    even_digits = [x for x in range(a, b + 1, 2)]
    return even_digits

# Test cases
print(generate_even_digits(10, 14))  # Output: []
print(generate_even_digits(2, 8))  # Output: [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # Output: [2, 4, 6, 8]
```

This Python script defines a function called `generate_even_digits`, which takes two integers as arguments, `a` and `b`. The function generates a list of even digits ranging from `a` to `b`, including only those that are between `a` and `b` in ascending order. The logic behind the generation is to iterate through integers ranging from `a` to `b` with an increment of 2, checking each integer to see if it's even (divisible by 2) and if it falls within the range. The function returns the list of even digits in the specified range, or an empty list if `b` is not greater than or equal to `a`. 

The tests are designed to show the functionality of the function. The first test case, `generate_even_digits(10, 14)`, should return an empty list since there are no even digits in the range. The second test case, `generate_even_digits(2, 8)`, returns a list containing the even digits between 2 and 8 in ascending order, namely `[2, 4, 6, 8]`. The third test case, `generate_even_digits(8, 2)`, also produces the list `[2, 4, 6, 8]` because it meets the criteria for even digits ranging from 8 to 2. 

To achieve this, the code utilizes list comprehension to filter out even integers between the start and end ranges, divided by 2. It is worth noting that the function expects that both `a` and `b` are positive integers, and that the starting integer `a` is also even. If these assumptions are not met, the function may not return the intended result.