```python
def multiply(a, b):
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers as input and returns the product of their unit digits, where the unit digit is the digit at the last position of the number. The function achieves this by using the `-1` indexing indexer syntax to extract the last digit of each number. The extracted digits are converted to integers using `int()` and then multiplied together. 
The assumption that input is always valid regards the legality of the inputs. Any non-integer numbers, or values that are not digits will result in a violation of this assumption. 

This function assumes that valid inputs will be provided and will return the product of the unit digits of the two inputs. 

The code passes the given tests of the problem statement and any edge cases such as negative numbers, or same-digit numbers.