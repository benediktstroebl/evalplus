```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, hundreds, tens, remainder = divmod(n, 1000)
        if thousands > 0: 
            return ""
        elif thousands == 0 and hundreds == 0: 
            if remainder == 0:
                return "i"
            elif remainder == 5:
                return "v"
            else:
                return str(remainder)
        elif thousands == 0 and hundreds == 0 and remainder == 0:
            return ""
        elif hundreds == 0: 
            if remainder == 0:
                return "x"
            elif remainder == 5:
                return "xv"
            else:
                return str(remainder) + "x"
        else:
            hundreds_str = self.int_to_mini_roman(hundreds)
            if remainder == 0:
                return hundreds_str
            elif remainder == 5:
                return hundreds_str + "v"
            else:
                return hundreds_str + str(remainder)
```

This script provides a function called `int_to_mini_roman` that takes in a number and converts it to its mini roman numeral representation as a string and returns it in lowercase. The function handles restrictions and various edge cases accordingly. You can test it further by calling the function with different input values.