Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > '9' or char < '0':
            if char == '-':
                odd_count += 1
            else:
                even_count += 1
        else:
            if int(char) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
```

This function first converts the input num to a string, then iterates through each character in the string. It differentiates between digits and non-digits, counting odd non-digit characters as odd and even non-digit characters as even, and counting digits based on whether they are even or odd.

If the input is zero, it returns (0, 0) as per the example provided in the prompt. 

Feel free to modify this to suit your needs or add additional tests to ensure its correctness. Let me know if you'd like more details or have additional questions!