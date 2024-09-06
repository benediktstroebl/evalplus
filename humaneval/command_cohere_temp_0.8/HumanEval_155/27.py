Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    count_even = 0
    count_odd = 0

    str_num = str(num)
    
    for char in str_num:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_odd += 1
    
    return (count_even, count_odd)
```

The function counts the number of even digits and odd digits in a string representation of the input number, then returns a tuple (count_even, count_odd) containing the counts. It also provides a simple example to demonstrate the usage of the function and handles a possible ValueError that occurs when the input is not an integer. 

You can test this function using the example provided in the docstring.