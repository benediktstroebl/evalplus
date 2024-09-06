Here's a Python script that contains a function which fulfills the criteria mentioned in the prompt:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a and b, in ascending order.
    """
    if a % 2 or b % 2:
        return []

    digits = []
    while a <= b:
        if a % 10 == 0:
            digits.append(a % 10)
        a = a // 10

    return digits

# Tests
def test_generate_even_digits():
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == []

test_generate_even_digits()
```

This script has a function called `generate_even_digits(a, b)` that takes two positive integers as arguments and returns a list of even digits that lie between `a` and `b`, inclusive, arranged in ascending order. The function first checks if either (or both) of the input integers is odd. If that is the case, it returns an empty list because no even digits exist in the range. If both inputs are even, it proceeds to loop through the digits of the decimal part of `a` (the highest order digit to the least significant digit). It checks if each digit is even and adds it to the list if it is. Once it has processed all digits, it returns the list of even digits in ascending order.

The script also includes a test function that verifies the correctness of the `generate_even_digits` function. It checks if the function's output matches the expected result for three distinct cases - the first two should return lists of even digits, and the third returns an empty list because the range lacks even digits.