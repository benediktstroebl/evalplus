```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as input and returns the product of their unit digits. The unit digit is the digit in the ones place, which is retrieved by using the expression `int(str(a)[-1])`. The function is then tested with the examples given in the problem prompt. 
Let's go over the examples provided: 
1. `multiply(148, 412)` returns `16` due to the unit digits of `148` and `412` being '1' and '6' respectively. 
2. `multiply(19, 28)` returns `72` due to the unit digits of `19` and `28` being '9' and '2' respectively. 
3. `multiply(2020, 1851)` returns `0` due to both `2020` and `1851` ending in '0'. 
4. `multiply(14, -15)` returns `20` due to the unit digits of `14` and `-15` being '4' and '5' respectively. 

The function is designed to handle any valid input and will always return the product of the unit digits of the two input integers. We assumed that the input is always valid, so there is no need for additional checks. 
If you would like to see the tests included, please let me know!