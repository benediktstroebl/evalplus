Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp_num = abs(num)
    
    while temp_num != 0:
        digit = temp_num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        temp_num = temp_num // 10
    
    return (count_even, count_odd)
```

This function counts the number of even and odd digits in an integer and returns a tuple with the respective counts. It begins by calculating the absolute value of the input num and storing it in a variable called temp_num. Then, it iterates through temp_num, checking each digit's parity and incrementing the appropriate count variable. Finally, it returns a tuple containing (count_even, count_odd).

Here is a markdown code block of concise unit tests for the function even_odd_count to validate its correctness across different input scenarios:
```python
# Test Case: [description, input, expected output]
test_cases = [
    ("Test for single-digit numbers", -1, (1, 0)),
    ("Test for single-digit numbers", 1, (0, 1)),
    ("Test for double-digit numbers", 12, (1, 1)),
    ("Test for triple-digit numbers", 123, (1, 2)),
    ("Test for multiple-digit numbers", 2017, (2, 3)),
    ("Test for decimal numbers", 12.345, (1, 1)),
    ("Test for zero", 0, (0, 0)),
    ("Test for negative numbers", -123, (1, 2)),
]

for description, input, expected in test_cases:
    output = even_odd_count(input)
    assert output == expected, f"For {description}, expected {expected}, but got {output}"
```

These tests cover a range of scenarios, including single- and multi-digit integers, decimal points, and negative numbers. Each test is described with a context sentence, and the expected output is provided for validation. By executing these tests using a testing framework like pytest, you can confidently verify the functionality of the even_odd_count function.  By executing these tests using a testing framework like pytest, you can confidently verify the functionality of the even_odd_count function.  If you want to optimize this script in terms of complexity, let me know, and I'll be glad to provide an alternative method to achieve the same results with a better time complexity, more specifically, O(log(n)) time complexity where n is the number expressed in its absolute value.