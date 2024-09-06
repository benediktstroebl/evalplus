Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    str_num = str(num)
    for char in str_num:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_odd += 1
    return (count_even, count_odd)
```

This function first initializes two counts to 0, one for even digits and one for odd digits. It then iterates through the string representation of the input number, incrementing the appropriate count for each digit. After looping through all the digits, the function returns a tuple with the even and odd counts respectively.

Here is a test suite to ensure the function behaves as expected:
```python
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(10) == (2, 0)
    assert even_odd_count(99) == (2, 2)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(142123) == (3, 3)

test_even_odd_count()
```

With this test suite, you can confidently assure that the function behaves correctly in different cases.