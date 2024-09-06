Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_odd += 1
    return (count_even, count_odd)
```

This function first initializes two counters, count_even and count_odd, to 0. It then iterates through the characters of the string representation of num and increments count_even if the character is an even digit ('0', '2', '4', '6', '8') and increments count_odd if the character is an odd digit ('1', '3', '5', '7', '9'). Finally, the function returns a tuple containing count_even and count_odd.

Here is an example of how to use this function:
```python
print(even_odd_count(123))  # Output: (1, 2)
print(even_odd_count(-12))  # Output: (1, 1)
```

This will output:
```bash
(1, 2)
(1, 1)
```

The function also handles the case when num is 0, returning both counts as 0. Feel free to modify the function or the test cases to fit your needs. Let me know if you would like me to explain any part of the code in more detail, or if you'd like to cover any other related topics!