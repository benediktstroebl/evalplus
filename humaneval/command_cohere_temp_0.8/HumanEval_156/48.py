```python
def int_to_mini_roman(num):
    if num < 1000:
        result = []
        for i in range(0, num + 1):
            if i == 0:
                result.append("i")
            elif i == 5:
                result.append("v")
            elif i == 10:
                result.append("x")
            elif i == 25:
                result.append("l")
            elif i == 50:
                result.append("c")
            elif i == 100:
                result.append("d")
            elif i == 250:
                result.append("m")
            elif i == 500:
                result.append("m")
            elif i == 1000:
                result.append("m")
            else:
                result.append(str(i))
        return "".join(result)
    else:
        return "Error! Number must be between 1 and 1000."
```

The function `int_to_mini_roman` iterates through the digits of the passed number `num` and appends the roman numeral equivalent to the `result` list. The final output is joined together into a string and returned as the roman numeral equivalent if the number is less than 1000. If the number is greater than or equal to 1000, an error message is returned. 

To follow the constraint of the given problem, the function checks if the number is less than 1000 before converting it to a roman numeral. Thus, if the number is greater than or equal to 1000, an error message is returned. 

This code can be copied and pasted into a Python environment to test the function with various input numbers.