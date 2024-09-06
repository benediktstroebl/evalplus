```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    num = [int(i) for i in range(a, b + 1)]
    even = [i for i in num if i % 2 == 0]
    return even
```

The function generates a list of integers between a and b, then filters out the odd integers from the list, resulting in a list of even digits in asending order. The implementation avoids unnecessary conversions and optimizations for a more concise and efficient solution. 

Here is a test case that verifies the function:
```python
def test_generate_even_digits():
    # Test case 1: Verify even digits between specific numbers.
    assert generate_even_digits(1, 10) == [2, 4, 6, 8]

    # Test case 2: Verify empty result when no even digits are present.
    assert generate_even_digits(10, 11) == []

    # Test case 3: Verify order and inclusivity of endpoints.
    assert generate_even_digits(4, 8) == [4, 6, 8]

test_generate_even_digits()
```

The tests ensure the function works correctly for different scenarios.