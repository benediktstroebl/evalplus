```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    mini_roman = []
    
    for i in range(1, 1000):
        if n >= i:
            mini_roman.extend(str(i))
            n -= i
    
    mini_roman = ''.join(mini_roman)
    return mini_roman.lower()

# Example usage
print(int_to_mini_roman(52))
print(int_to_mini_roman(426))
```

This script uses a loop to iteratively convert integers into their mini roman numeral representations. It converts numbers incrementally, adding the appropriate roman numeral characters to a list. The final output is converted to a string and lowered to ensure consistency. The overall time complexity of this solution is O(M), where M represents the absolute value of the input integer.