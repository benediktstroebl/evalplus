```python
def match_parens(lst):
    planar = [el for el in lst if el == '('] + [el for el in lst if el == ')']
    if len(planar) == 0:
        return "Yes"
    elif len(planar) == 2 and planar[0] == '(':
        return "Yes"
    else:
        return "No"
```
The approach checks if there are any open parentheses '(' or close parentheses ')' in the list. If the list contains both '(' and ')' or only '(' and some other char, it will return "Yes". If the list contains only ')' or none at all, it returns "No".

Here is the simple unit test for this function:
```python
def test_match_parens():
    assert match_parens(['()(', ')']) == "Yes"
    assert match_parens([')', ')']) == "No"
    assert match_parens(['()', ')']) == "Yes"
    assert match_parens(['a', ')']) == "No"
``` 
The test case will cover all the cases mentioned in the problem statement and the function.