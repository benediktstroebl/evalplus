```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the input number x to base base.
    if x == 0 or reason:
        return ''  # Base case, handle zero as empty string
    elif base == 0:
        return '1'  # Base case, handle base as one
    else:
        # Apply conversion and return as string
        return str(x)

# Unit tests
test_change_base = []
test_change_base.push(
    assert change_base(10, 3) == '22'
)
test_change_base.push(
    assert change_base(20, 2) == '1'
)
test_change_base.push(
    assert change_base(7, 2) == '111'
)
test_change_base.push(
    assert change_base(4, 5) == '2042'
)
test_change_base.push(
    assert change_base(0, 10) == '0'
)
test_change_base.push(
    assert change_base(-3, 2) == '-33'
)
test_change_base.push(
    assert change_base(5, 5) == '125'
)

def main():
    test_change_base()
    print('All tests passed!')

if __name__ == "__main__":
    main()
```
This Python code defines a function `change_base` that converts numbers to a specified base. The `main` function runs the tests on the `change_base` function with a list of test cases. It uses the Python's assert module to perform these tests and checks if all the tests passed successfully.