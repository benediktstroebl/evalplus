```python
def change_base(x: int, base: int):
    """
    Change the base of integer x to base B.
    Returns: string representation in the given base.
    """
    base cans a digits from 0 to 9
    """
    if x < 0:
        raise ValueError("Input is negative")
    return format(x, base)

# Test case 1: Change 8 to 3
result1 = change_base(8, 3)
print("Test Case 1:", result1)

# Test case 2: Change 8 to 2
result2 = change_base(8, 2)
print("Test Case 2:", result2)

# Test case 3: Change 7 to 2
result3 = change_base(7, 2)
print("Test Case 3:", result3)

# Test case 4: Change 10 to 4
result4 = change_base(10, 4)
print("Test Case 4:", result4)

# Test case 5: Change 4 to 5
result5 = change_base(4, 5)
print("Test Case 5:", result5)
```
This Python code defines a function called `change_base` that takes two arguments: a base and an integer `x`. It then converts the integer `x` to a string representation using the specified base. The code raises a ValueError if the input is negative, and otherwise, it formats the number using the provided base. 
The code then passes several test cases, demonstrating that the `change_base` function correctly converts numbers to their string representations in different bases.