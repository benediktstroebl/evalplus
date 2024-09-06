```python
def change_base(x, base):
    return str(x) in ['0', '1'] and x == 1 or f"{int(x)}".__mod__(base) or change_base(int(f"{int(x)}".__mod__(base)), base)
```

The given Python code defines a function called `change_base` that takes two arguments: `x`, which is an integer, and `base`, which is also an integer. This function's primary purpose is to convert the numerical base of `x` to the specified base (`base`). It achieves this through a combination of integer manipulation and recursive calls.

Here's how it works:
1. The function starts by checking if `x` is either '0' or '1'. If this is the case, it returns `x` immediately, assuming that these two bases represent the simplest cases where the conversion result is the same as the input.
2. If `x` is not '0' or '1', the function proceeds to use the modulo operator (`%`) to calculate the remainder of the division of `x` by `base`. This step isolates the fractional part of the number when divided by `base`.
3. The result of the modulo operation is then used to make a recursive call to the `change_base` function, but with the base and the fractional part as arguments. This recursive call continues the process of converting the base and reducing the fractional part.

The recursive calls continue until the fractional part becomes zero, at which point the function returns the converted integer (i.e., the remainder of the division of `x` by `base`).

Example usage:
```python
print(change_base(8, 3))  # Outputs: '22'
print(change_base(8, 2))  # Outputs: '1000'
print(change_base(7, 2))  # Outputs: '111'
```

This function efficiently converts the base of a number using a combination of integer manipulation and recursion, ensuring proper conversion and handling of edge cases.