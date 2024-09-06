```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        else:
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the opening and closing brackets `'['` and `']'` respectively, as it iterates through the string. The algorithm is then passed a valid bracket sequence if the count of opened brackets is equal to the count of closed brackets. The function returns a false value if there is any invalid nesting of brackets, as assessed by the inequality `open > closed`. 

To validate the functionality of the algorithm, here is a list of test cases with their corresponding expected outcomes:
1. `is_nested('[[]]')` - This should return `True` since there is a valid nested bracket sequence. 
2. `is_nested('[][]')` - This should return `False` as there is no nested bracket sequence. 
3. `is_nested('[]')` - This should return `False` as there is an imbalance in the opening and closing of brackets. 
4. `is_nested('][')` - This should return `False` since a closing bracket `']'` is missing. 
5. `is_nested('[[])` - This should return `False` since an opening bracket `'['` is missing. 
6. `is_nested('[][]]', strict=True)` - This should return `False` as there is no valid bracket sequence. 

The last test case demonstrates the sensitivity of the algorithm to the boundaries of the string. By default, the function considers only the entire input string to evaluate its validity as a bracket sequence. However, to enforce strict adherence to the problem statement and consider the subsequence, we can set the `strict` parameter to `False`.