```python
def match_parens(lst):
    open_tup = tuple(map(ord, lst[0]))
    close_tup = tuple(map(ord, lst[1]))
    if open_tup == close_tup:
        return "Yes"
    return "No"
```

This Python script solves the given problem by comparing the two input strings at the character level, transforming them into tuples of their corresponding open or close parentheses ordinals. It then checks if the two tuples are equal, which would indicate that the input strings can be concatenated in some order to form a balanced parentheses string. If the tuples are equal, it returns "Yes"; otherwise, it returns "No". This approach ensures that any balanced parentheses combinations will be recognized as valid.