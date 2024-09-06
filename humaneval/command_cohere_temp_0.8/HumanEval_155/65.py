Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    count = 0
    for digit in str(abs(num)):
          if int(digit) % 2 == 0:
              count += 1
    return count, len(str(abs(num))) - count
```

The script provides a function that takes an integer num as input and returns a tuple. The first element of this tuple is the count of even digits in the absolute value of num, and the second element is the count of odd digits in the absolute value of num. 

To achieve this, the function first converts the absolute value of num to a string, which is then iterated through to check if each digit is even or odd. The counts are stored respectively, with the total count of digits calculated through string subtraction. 

The module on which the `abs()` function and the `tuple()` function is built is assumed to be the `builtins` module.

Note that this code assumes that the input integer is non-negative, and the behavior for negative inputs is left undefined. However, the provided example tests demonstrate the expected behavior for different inputs. 
If the input is a string or has non-digit characters, the function will raise a TypeError. Also, the function assumes that the input integer is already in its absolute form, so it may require additional preprocessing for scenarios where this is not the case. P