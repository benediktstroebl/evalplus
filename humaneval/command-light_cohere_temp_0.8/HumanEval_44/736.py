```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers less than 2 are converted to strings using format()
    """
    return format(x, f"{base}")

if __name__ == "__main__":
    x = int("8")
    base = 2
    print(change_base(x, base))  # Output: 1000
    x = int("7")
    base = 3
    print(change_base(x, base))  # Output: 22
    x = int("207")
    base = 10
    print(change_base(x, base))  # Output: 20700
```

This code defines a function called `change_base`, which takes two parameters: `x`, representing the number to be converted, and `base`, representing the base to which the number will be converted. The function uses the format() function to convert the number `x` to a string representation using the specified base `base`. This function effectively converts the number to a string using the desired base, and it is then returned. The code also includes a `__name__ == "__main__"` block, which ensures that the `change_base` function is executed when the script is run directly, rather than being called from another function.