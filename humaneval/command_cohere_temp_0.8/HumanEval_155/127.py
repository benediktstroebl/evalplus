Here's a Python script that contains a function called even_odd_count, defined to take in an integer and return a tuple with the counts of odd and even digits in the given integer:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            even_count += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            odd_count += 1
    return (even_count, odd_count)
```

The function initially checks if the input is an integer and then converts it to a string to be able to iterate through the digits. It uses nested if-elif statements to determine if each digit is even or odd and increments the respective counter. Finally, it returns a tuple containing both counters.