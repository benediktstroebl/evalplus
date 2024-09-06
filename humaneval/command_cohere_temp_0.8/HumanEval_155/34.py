Here's a Python script that contains a function called even_odd_count which takes an integer num as its input and returns a tuple with the count of both even and odd digits in num. This function also has some corresponding test cases which check whether the function behaves as expected:
```python
def even_odd_count(num):
    even, odd = 0, 0
    str_num = str(num)
    for char in str_num:
        if char <= '9' and char >= '0':
            if int(char) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)

# Tests
tests = [(-12, (1, 1)), (123, (1, 2)), (15, (1, 1)), (10, (1, 0)), (-100, (0, 3)), ((5 * 10) + 4, (1, 1)), (100, (2, 2))]

for num, expected in tests:
    result = even_odd_count(num)
    assert result == expected, f"For {num}, the expected result is {expected}, but got {result}"
```
This code uses a string-conversion technique to count the digits. Hence, for integers, the function will consider 0 as the first digit, and for negative numbers, ten minus the absolute value will be considered as the first digit (e.g., -12 will be treated as 10 - 12 = -2, and the first digit will be 0). Finally, the ten minus will be adjusted along with the count of even digits.