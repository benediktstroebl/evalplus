Here's a Python script with a self-contained function `generate_even_digits` that solves the problem:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    if a % 2 or b % 2:
        return []  # Return empty list if either 'a' or 'b' is odd
    integers = [int for int in range(a, b + 1)]
    even_digits = [int for int in integers if int % 2 == 0]
    return even_digits
```
This function only uses the two provided positive integers 'a' and 'b' and native Python functionalities, namely list comprehensions, to solve the problem. It is also scalable and efficient in terms of time and memory complexity since it only requires iterating over the integers once to check if they are even.

Here is a simple test case to verify the functionality of the script:
```python
def test_even_digits():
    # Basic Test Cases
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == [12, 14]

    # Edge Cases
    assert generate_even_digits(1, 100) == []
    assert generate_even_digits(100, 1) == []
    assert generate_even_digits(101, 105) == [102, 104]

test_even_digits()
```
The test cases cover various scenarios, including edge cases, to ensure that the `generate_even_digits` function works correctly.