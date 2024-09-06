```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    mini_roman = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_num = [1000, 950, 500, 450, 100, 95, 50, 45, 10, 9, 5, 4, 1]
    
    result = []
    
    for i in range(len(mini_roman)):
        while n >= mini_roman[i]:
            result.append(roman_num[i])
            n -= mini_roman[i]
    
    result = ''.join(result)
    return result.lower()
```

The algorithm works by using two arrays: `mini_roman` and `roman_num`, which store the corresponding roman numerals in reverse order. The algorithm iterates over the two arrays, slowly building the roman numeral string as the value of `n` descends. An additional step molds the resultant string into lowercase.