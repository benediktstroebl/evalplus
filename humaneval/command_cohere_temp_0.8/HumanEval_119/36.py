```python
def match_parens(lst):
    open_tup = tuple(opening for opening, _ in lst)
    close_tup = tuple(closing for _, closing in lst)
    if open_tup == close_tup:
        return "Yes"
    return "No"
```

The code defines a function `match_parens` that takes in a list of two strings, each containing only open or close parentheses. The function constructs a tuple of the opening parentheses and a tuple of the closing parentheses, then compares the two tuples. If the two tuples are equal, meaning that the opening and closing parentheses are balanced, the function returns "Yes" indicating that a good string can be formed by concatenating the two input strings in some order. Otherwise, if the opening and closing parentheses are not balanced, indicating no way to form a good string, the function returns "No". This code efficiently determines the feasibility of forming a balanced string by concatenating the two input strings, ensuring proper synchronization of opening and closing parentheses.