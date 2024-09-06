Here's a Python script that contains a function called even_odd_count, defined to take in an integer num and return a tuple containing the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    
    count_even = 0
    count_odd = 0
    
    str_num = str(num)
    
    for char in str_num:
        if char == '0' or char == '1' or char == '2' or char == '3':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        elif char == '4' or char == '5':
            if char == '4':
                count_even += 1
            else:
                count_odd += 1
        elif char == '6' or char == '7' or char == '8' or char == '9':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        elif char == ' ':
            pass
        else:
            raise ValueError("Invalid input")
    
    return (count_even, count_odd)
```

This Python script defines a function even_odd_count that takes an integer num as input and returns a tuple containing the counts of even and odd digits in num. It ensures the input is an integer and then converts it to a string. The script then iterates through each digit in the string, categorizing them as even or odd and updating the respective count variables. After processing all digits, the function returns the calculated counts in a tuple.