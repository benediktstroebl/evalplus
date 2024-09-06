Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i == '0' or i == '6' or i == '8' or i == '4':
            count_even += 1
        elif i == '1' or i == '3' or i == '5' or i == '7' or i == '9':
            count_odd += 1
    return (count_even, count_odd)
```

This script includes a test case for the function even_odd_count to ensure its functionality:
```python
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(456) == (2, 2)
    assert even_odd_count(789) == (2, 3)
    assert even_odd_count(0) == (0, 0)
```

Therefore, the even_odd_count function's behavior is to return a tuple of two elements (count_even, count_odd), where count_even is the number of even digits encountered in the decimal representation of the integer `num`, and count_odd is the number of odd digits encountered. This is illustrated by the use of the digits 0, 6, 8, and 4 to represent even digits, and the digits 1, 3, 5, 7, and 9 to represent odd digits.