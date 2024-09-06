```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        thousands, ones = divmod(n, 1000)
        hundreds, tens = divmod(thousands, 100)
        tens = (tens + 5) // 5
        tens = ("i" * tens) + "x" * (tens == 0)
        hundreds = "c" * hundreds + tens_to_mini_roman(ones)
        return hundreds + "m" * (thousands > 0)

def tens_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n == 2:
        return "ii"
    elif n == 3:
        return "iii"
    elif n == 4:
        return "iv"
    elif n == 5:
        return "v"
    else:
        return "x" * (n - 5)
``` 

This code uses a recursive approach for converting integers to mini roman numerals which is a string representation of roman numerals but with the following restrictions:
1. Each roman numeral is represented by a lowercase letter: `i`, `v`, `x`, `l`, `c`, `d`, `m` 
2. There is no difference between `i`, `v`, `x` so they can be used interchangeably. 

The function uses tuple decomposition to extract thousands, hundreds, and ones so that the appropriate numerals can be used to build the mini roman numerals based on the value of the thousands, hundreds, and ones variables. 

Taking hundreds as an example, if ones was 3, then hundreds would be "ciii" which would be transformed to "iii" following the mini-roman numeral rules. 

The thousands variable is important in determining whether to use thousands by checking if thousands is greater than 0 in which case it would add the letter "m" to the end of the string value of the numeral. 

To test this code please run `python -m doctest -v ` and copy and paste this code into a Python file and run the tests.