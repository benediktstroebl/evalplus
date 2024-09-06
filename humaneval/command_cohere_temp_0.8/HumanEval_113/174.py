```python
def number_of_odd_digits(string_list):
    # Count the total number of odd digits across all strings
    total_odd_digits = sum(char for char in string_list if char % 2 != 0)
    
    # Format the output strings
    output_strings = ["the number of odd elements in the string {} of the input.".format(i + 1) for i in range(len(string_list))]
    output_strings = [string.replace('n', total_odd_digits)
                        .replace('n', 'n' if total_odd_digits == 1 else 's')
                        .replace('1', str(i + 1))
                        for i, string in enumerate(output_strings)]
    return output_strings
```

To use this function, you can call it with a list of digit strings, and it will return a list of formatted strings indicating the count of odd digits in each string. 
For example:
```python
print(number_of_odd_digits(['1234567', '3', '11111111']))
```

The expected output is:
```
['the number of odd elements 4 in the string 1 of the input.', 'the number of odd elements 1 in the string 1 of the input.', 'the number of odd elements 8 in the string 8 of the input.']
```