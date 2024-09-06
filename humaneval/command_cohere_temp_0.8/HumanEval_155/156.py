Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > "9":
            continue
        elif char == "0":
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
```

This script defines a function even_odd_count that takes a single parameter num. The function first converts the input num to a string and then counts the number of even and odd digits in this string. The function returns a tuple (even_count, odd_count) containing the counts of even and odd digits, respectively.

To test this function, you can run the following code, which checks if the function's outputs match the expected values for certain inputs:
```python
# Testing Suite
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (1, 1)
    assert even_odd_count(19) == (1, 1)
    assert even_odd_count(100) == (2, 0)
```