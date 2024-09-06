Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > "9" or char < "0":
            continue
        elif char % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
```

This function first converts the input num to a string, then iterates through each digit. It distinguishes between even and odd digits, incrementing the respective counters, and finally returns the counts as a tuple.

This code would be encased in a test block, and would typically be accompanied by assertions to ensure the function behaves as expected. Here's how the complete code would appear within a test block:
```python
def test_even_odd_count():
    # Test case for even and odd digits
    assert even_odd_count(11111) == (4, 3)

    # Test case for only even digits
    assert even_odd_count(2222) == (4, 0)

    # Test case for only odd digits
    assert even_odd_count(377377) == (0, 7)

    # Test case for a mixed digit number
    assert even_odd_count(123) == (1, 2)

```

This would help ensure the function behaves as expected for various cases.  This type of testing is instrumental in validating our code to ensure it behaves as anticipated.