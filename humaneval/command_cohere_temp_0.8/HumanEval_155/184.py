Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
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

This function will convert the input num into a string, and iterate through each digit to count the number of even and odd digits. Finally, it will return a tuple containing (even_count, odd_count). For example, input num = -12 will result in (1, 1), and input num = 123 will result in (1, 2).

To make this code more efficient and cleaner, we could do it without converting the number to a string, but assuming this is a small exercise, we are helping with readability and simplicity.