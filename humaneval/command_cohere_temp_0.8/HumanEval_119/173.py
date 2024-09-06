```python
def match_parens(lst):
    def shift(s):
        return s.replace('(', '').replace(')', '')
    
    def calc(s1, s2):
        return shift(s1 + s2) == shift(s2 + s1)
    
    return "Yes" if calc(*lst) else "No"
```

The function relies on two simple auxiliary functions: `shift` removes all open and close parentheses from a string, leaving only their counts; `calc` checks if the balance of parentheses is the same after concatenating the two strings in either order.

To use this code, you can simply call the function with the list of strings as follows:
```python
print(match_parens(['`(', '())`', '()']))  # Yes
print(match_parens(['`)`, '`(()`', ')'])  # No
```