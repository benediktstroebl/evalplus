```python
def separate_paren_groups(s): 
    """ 
    Separation of parenthesis groups into separate strings. 
    """
    balanced = True 
    spaces = 0
    ret = []
    for w in s: 
        if balanced: 
            if w == '(': balanced = False 
        else: 
            ret.append(w)
            balanced = True
        spaces += 1
    return ret 
# Example test cases 
test_cases = [
    "()", "( )", "( )( )", "())",
    "(( ))", "(( ))( )",
    "((()))"
]

for case in test_cases: 
    result = separate_paren_groups(case)
    assert len(result) == 1
    print(f"Case: {case}, Result:{result}, Should be: {case}")
```
Do you need anything else?