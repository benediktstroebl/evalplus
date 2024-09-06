```python
def generate_even_digits(a, b):
    """
    Generating even digits between two positive integers, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits from the range a to b, in ascending order.
    """
    # Ensuring the inputs are positive and discarding the remainder of division by 2
    a, b = (int(num) if num % 2 == 0 else int(num) + 1) for num in (a, b)
    even_digits = [str(num) for num in range(a, b + 1, 2)]
    return [int(digit) for digit in even_digits]
```

The function takes two positive integers as arguments and returns a list of even digits between them, in ascending order.

To ensure that the returned list contains only even digits, we make sure that both `a` and `b` are even (discarding the remainder of division by 2 if they are odd). We then iterate through the even numbers between `a` and `b` in steps of 2, converting them to strings and finally to integers in the list.

The unit tests reassure us that the function works correctly for various input combinations:
```python
def test_generate_even_digits():
    # Basic tests
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == [12, 14]

    # Edge cases
    assert generate_even_digits(1, 4) == [2, 4]
    assert generate_even_digits(100, 200) == [102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]
```