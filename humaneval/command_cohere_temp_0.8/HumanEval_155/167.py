Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > "9":
            if char % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            if int(char) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
```

This script defines a function even_odd_count that takes a single argument, num, representing an integer. It then converts this integer to a string, and iterates through each digit (including numeric and alphabetic characters). It increments the even_count variable if the current digit is even, and increments odd_count if the current digit is odd. Finally, the function returns a tuple containing the counts of even and odd digits.

Here is a simple test suite to ensure that the function behaves as expected:
```python
def test_even_odd_count():
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(111) == (0, 3)
    assert even_odd_count(10) == (1, 0)

test_even_odd_count()
```

Assuming you have placed this script in an environment that supports Markdown code blocks (like a Jupyter Notebook), you should be able to run the test suite by pressing the "Run" button in the code block that contains it.