```python
def change_base(x: int, base: int):
    """
    Changes the numerical base of input number x to base base and returns the string representation.

    :param{x int x, int base}
    """
    # code here
    return f"{x: {base}}"

# tests
test_change_base = []
test_change_base.py = [
    [
    "change_base(8, 3)", 3, "'22'"
    ],
    [
        "change_base(7, 5)", 5, "'177'"
    ],
    [
        "change_base(2, 16)", 16, "'FF'"
    ],
    [
        "change_base(10, 16)", 16, "'16'"
    ],
    [
        "change_base(15, 10)", 10, "'1500'"
    ]
]

print(test_change_base)
``` 
The code defines a function change_base that takes two arguments: a base and x, and converts x from the current base to base base. It then returns the final string representation of the number. 
The code also defines a series of test cases for the function. These tests check the test the print the test cases and the expected output for each case, which should match the output of the function.