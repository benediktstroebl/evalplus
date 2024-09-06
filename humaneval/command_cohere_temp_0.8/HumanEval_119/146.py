```python
def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')']
    if len(planar) == 0:
        return "Yes"
    elif len(planar) == 1:
        return "No"
    else:
        rem = match_parens(planar)
        if rem == "Yes":
            return "Yes"
        else:
            return "No"
```
The provided solution uses a recursive approach to solve the problem. The inner function only uses planar parentheses, i.e., those that are either '(' or ')' only. These are passed down the recursive call and alternately, ('(', ')') is swapped with ('/', ')'). If the inner function returns 'Yes', our function returns 'Yes' without further processing. Otherwise, it swaps all the '(' with ')' and vice versa because to match a '(' we need a ')' and vice versa. It then checks if the list has become empty, in which case it returns "Yes" or if the length is 1, in which case it returns "No". 

Here is the documentation for the outer function which calls the inner function with the planar parentheses list:
```python
def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')']
    if len(planar) == 0:
        return "Yes"
    elif len(planar) == 1:
        return "No"
    else:
        rem = match_parens(planar)
        if rem == "Yes":
            return "Yes"
        else:
            return "No"
```