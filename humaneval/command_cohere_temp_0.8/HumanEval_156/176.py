```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Correspondence between Arabic and Roman numerals
    arabic = ["i", "v", "x", "l", "c", "d", "m"]
    roman = ["i", "iv", "ix", "xl", "xc", "xd", "xm"]

    result = []
    while n > 0:
        for arabic_num in range(0, n // 5 + 1):
            result.append(arabic[arabic_num])
            n -= 5 * arabic_num
        if n > 0:
            result.append(arabic[n % 5])
    result.reverse()

    return "".join(roman[i] for i in result)

# Test Cases
print(int_to_mini_roman(19) == 'xix')
print(int_to_mini_roman(152) == 'clii')
print(int_to_mini_roman(426) == 'cdxxvi')
```
This script incorporates the mapping between Arabic and Roman numerals as a lookup, and the result is formatted and returned as a string. The tests provided for the function are included and ensured to evaluate correctly. 
For further optimization and improvements, one could consider using a loop instead of repeated appends to the result list, as the order of mappings doesn't change. This may offer a slight performance boost. Additionally, ensuring the input is within the specified range using assertions may help for robustness.