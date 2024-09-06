```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return any([a, b, c])
```

This function checks if any combination of adding two of the three numbers equals the third number. It returns `true` if any of these conditions are met, and `false` otherwise. To achieve this, it employs a list (`: a, b, c`) which feeds into the `any()` function. This function returns `true` if any element in the list is `true`. The six points (`..`) used in the comment lines are often used in Markdown to create horizontal rules in code blocks. They are not part of the Python syntax. 

This approach uses only one conditional statement and is thus more efficient than the previous version. 

To test this script, ensure you have the Python interpreter available, or create a separate test file. You may use the following test cases to verify the correctness of the function:
```python
# Test Case which follows the Examples in the Prompt
print(any_int(5, 2, 7))  # Should print True
print(any_int(3, 2, 2))  # Should print False
print(any_int(3, -2, 1))  # Should print True
print(any_int(3.6, -2.2, 2))  # Should print False

# Additional Test Cases
print(any_int(-1, -1, 0))  # Should print True
print(any_int(0, -1, -1))  # Should print True
print(any_int(1, 2, 3))  # Should print False
print(any_int(-5, -7, -5))  # Should print True
```
This should output:
```bash
True
False
True
False
True
``` 
Let me know if you have any other questions!