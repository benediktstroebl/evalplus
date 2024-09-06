Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8' or char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

This function converts the input num into a string and iterates through each digit. It checks if the digit is even or odd and increments the respective count accordingly. The function returns a tuple with the counts of even and odd digits.

To test this function, you can run the following code:
```python
# Testing the function against a few test cases
test_cases = [(-12,), (123,), (1234567890,), (-1,), (1,), (2017,), (555,), (37,)]
for n, expected in test_cases:
    result = even_odd_count(n)
    assert result == expected, f"For input {n}, expected {expected}, but got {result}"
```

This block of code tests the even_odd_count function against multiple test cases to ensure it returns the expected results.