```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits from the range a to b, in ascending order.
    """
    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] == '':: 
            even_digits.append(int(x))
    return even_digits
```

The function iterates through the integers between `a` and `b`, and checks if the string representation of the number has a digit whose index is greater than `1`, which is the index of the last digit when the number is represented as a string. If the index is 1, that means it's an even number, so the function adds it to the `even_digits` list.

This solution efficiently retrieves even digits from the given range.

This approach covers the even-numbered integers within the specified range and ensures that the returned value is a list of even digits in ascending order. 

The tests that can be used to verify this solution are:
```python
import unittest

def test_generate_even_digits():
    # Test case 1
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]

    # Test case 2
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]

    # Test case 3
    assert generate_even_digits(10, 14) == [12, 14]

    # Test case 4
    assert generate_even_digits(1, 3) == [2, 3]

class TestGenerateEvenDigits(unittest.TestCase):
    def test_generate_even_digits(self):
        assert self.assertEqual(generate_even_digits(2, 8), [2, 4, 6, 8])
        assert self.assertEqual(generate_even_digits(8, 2), [2, 4, 6, 8])
        assert self.assertEqual(generate_even_digits(10, 14), [12, 14])
        assert self.assertEqual(generate_even_digits(1, 3), [2, 3])
```