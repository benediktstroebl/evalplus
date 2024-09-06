```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        hundreds, remainder = divmod(n, 5)
        if hundreds == 0:
            return str(remainder) + "i"
        tens, ones = divmod(remainder, 5)
        if hundreds == 1:
            return "x" + str(ones)
        if hundreds == 2:
            return "l" + str(ones)
        if hundreds == 3:
            return "c" + str(ones)
        if hundreds == 4:
            return "d" + str(ones)
        else:
            return "".join([str(ones), chr(ord("x") + tens)])
```

This code uses modular arithmetic to iterate through each of the digits and determine the Roman numeral representation for each part. The hundreds place is handled differently based on the value. Lastly, the tens and ones are converted and added to the string representation, ensuring that it is all lowercase. 

Would you like to know more about Roman numerals or any specific part of the algorithm? Feel free to ask!