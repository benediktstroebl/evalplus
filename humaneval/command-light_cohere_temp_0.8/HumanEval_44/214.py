```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base B"""
    # check base is valid
    assert base != 0, f'base cannot be zero, use invalid_base function!'
    # convert to string representation
    return format(x, base)

def invalid_base(base: int) -> None:
    """Raise error if base number is not valid"""
    assert 0 < base <= 36, 'base must be between 2 and 36'
    raise ValueError('Invalid base number')

def main():
    base = 10  # set base to 10
    x = 8  # set x value

    print(change_base(x, base))  # calls function and prints output

if __name__ == "__main__":
    invalid_base(2)  # call invalid_base function with invalid base
    main()  # call main function
```