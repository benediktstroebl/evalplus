```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:]+digits[:-shift] if len(digits) < shift else digits[shift:]+digits[:shift]
```
The code works by first converting the integer `x` to a string using `str(x)`. Then, it extracts a substring of the string from the end of the string (`digits[-shift:]`), and the beginning of the string (`digits[:-shift]`), depending on the relation between the shift and the length of the number. If the shift is greater than the length of the number, it shifts the digits from the beginning to the end of the number, instead of the other way around. 

Here is an example usage of the function:
```python
circular_shift(12, 1) # "21"
circular_shift(12, 2) # "12"
circular_shift(518, 3) # "518"
circular_shift(518, 10) # "518"
```
This would output:
```
21
12
518
518
```

The function handles the edge case of shifting more times than the number of digits, and provides a clear behavior for such cases.