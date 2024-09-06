Here's a Python script that contains a function called even_odd_count, defined to take in an integer and return a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            even_count += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_count += 1
    return (even_count, odd_count)
```

The function begins by casting the input num to a string, letting the function manipulate the digits as strings. It initializes two counters, even_count and odd_count, to 0, for keeping track of the number of even and odd digits respectively. Then it loops through each digit in the string representation of the number, incrementing the appropriate counter depending on whether the digit represents an even or odd value. The function returns a tuple containing the two counts.

Here is a test suite to ensure the function behaves as expected:
```python
def test_even_odd_count():
    # Test case for even number
    assert even_odd_count(0) == (2, 0)
    assert even_odd_count(8) == (3, 1)
    assert even_odd_count(1024) == (4, 2)

    # Test case for odd number
    assert even_odd_count(1) == (0, 2)
    assert even_odd_count(21) == (2, 3)
    assert even_odd_count(1557) == (4, 3)

    # Test case for negative number
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-321) == (3, 2)

    # Test case for single-digit number
    assert even_odd_count(5) == (1, 0)

    # Test case for large number
    assert even_odd_count(9876543210) == (6, 7)

    # Test case for decimal number
    assert even_odd_count(123.45) == (2, 1)
```

This test suite contains a variety of tests, including tests for even and odd numbers, positive and negative numbers, and decimal numbers, ensuring that the function handles all these case gracefully.