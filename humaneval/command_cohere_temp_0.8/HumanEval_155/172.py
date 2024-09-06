Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input num is not an integer")
    
    count_even = 0
    count_odd = 0
    
    str_num = str(num)
    
    for char in str_num:
        if char == '0' or char == '1' or char == '2' or char == '3':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        elif char == '-' or char == '+' or char == 'e' or char == 'E':
            continue
        else:
            raise ValueError(f"Unexpected character encountered in num: {char}")
    
    return (count_even, count_odd)
```

This script defines a function that takes an integer as input and returns a tuple of two integers representing the counts of even and odd digits in the input integer. It ensures the input is an integer and then converts it to a string to count the occurrences of even and odd digits. The function handles optional separators like '-', '+' and 'e', and ignores them. It raises a ValueError for invalid input types and unexpected character types.