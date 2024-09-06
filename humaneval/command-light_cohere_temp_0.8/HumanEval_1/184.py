```python
def separate_paren_groups(s): 
    return [c for c in s.gap if c.isspaceopen openbr('(',')]}

# Test cases
for test in [
    "()\)\)".strip()  , 
    " (( ) )",
    # spaces allowed 
    "  (  )   "
    
]: 
    print(separate_paren_groups(test)) == ['.')  , '()', '()']
```
Do you need help with any other aspect of Python programming?