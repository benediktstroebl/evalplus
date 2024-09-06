```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base b.
    Base must be a current of > 0, and x must be greater than 0.
    """
    def __init__(self, x, base):
        if base <= 0 or x <= 0:
            raise ValueError("Both base and number must be > 0")
        self.x = x
        base = base

    # Use the built-in int() to ensure x is an integer
    if not isinstance(x, int):
        raise TypeError("Input must be an integer")

    # Implement the change_base function
    return self.format(x, x, base)

    # Test cases
    if change_base(8, 3) == '22':
        print("Test passed")
    if change_base(8, 2) == '1000':
        print("Test passed")
    if change_base(7, 2) == '111':
        print("Test passed")
    else:
        print("Test failed")
    if change_base(7, 5) == '33':
        print("Test passed")
    else:
        print("Test failed")
    ```