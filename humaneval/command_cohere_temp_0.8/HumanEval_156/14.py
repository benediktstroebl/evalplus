```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, remainder = divmod(n, 5)
        if hundreds == 0:
            return str(remainder) + "i"
        tens, ones = divmod(remainder, 5)
        if tens == 0 and ones == 0:
            return "xv"
        if tens == 0:
            return str(ones) + "i"
        if ones == 0:
            return str(tens) + "x"
        return str(tens) + str(ones) + "i"
```

The approach used in the code above makes good use of the properties of the problem and the roman numerals, it iterates through the value converting relevant numbers into roman numerals based on the rules of subtraction. Please note that this solution has a time complexity of O(log(n)) due to the divisions and modulo operations, it is not the most efficient solution possible however it is a straightforward application of the properties of roman numerals.