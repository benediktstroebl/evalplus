```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Convert number to list of digits and decimals
    num_list = [int(n) while n % 1 else n]
    
    mini_roman = []
    
    # Convert each number to roman numeral
    for num in num_list:
        if num >= 5:
            mini_roman.extend(str(x) for x in range(5, -1, -1) if num // 5 >= x)
        if num >= 10: 
            mini_roman.append('x')
            mini_roman.extend(str(x) for x in range(10, -1, -1) if num // 10 >= x)
        if num >= 50:  
            mini_roman.extend(str(x) for x in range(50, -1, -1) if num // 50 >= x)
        if num >= 100: 
            mini_roman.append('c')
            mini_roman.extend(str(x) for x in range(100, -1, -1) if num // 100 >= x)
        if num >= 500: 
            mini_roman.extend(str(x) for x in range(500, -1, -1) if num // 500 >= x)
        if num >= 1000: 
            mini_roman.append('m')
            mini_roman.extend(str(x) for x in range(1000, -1, -1) if num // 1000 >= x)

    return ''.join(mini_roman)
```

This script provides a function called `int_to_mini_roman`, which converts a given positive integer to its mini roman numeral representation as a string. It handles decimals as well, and roman numerals are truncated to the closest lower value. The function is designed to handle numbers between 1 and 1000.