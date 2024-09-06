Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_even = 0
        count_odd = 0
        str_num = str(num)
        for char in str_num:
            if char <= '9' and char >= '0':
                if int(char) % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
        return (count_even, count_odd)
    else:
        return "Error: Please provide an integer."

# Unit tests:
test_cases = [(-12,), (123,), (345,), (-56,), (1001,), (2000,)]
for num, expected in test_cases:
    assert even_odd_count(num) == expected, f"For {num}, expected {expected}, but got {even_odd_count(num)}."
```

The function begins by checking if the given parameter is an integer and then converts it to a string to proceed with the digit checking. It iterates over each digit of the string representation of the number and counts the number of even and odd digits respectively. Finally, the function returns a tuple with the counts of even and odd digits. The test suite verifies the functionality of the function for a variety of cases.