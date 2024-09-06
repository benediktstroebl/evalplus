```python
def match_parens(lst):
    def shift_brackets(brackets):
        out = []
        opening = 1 if brackets[0] == '(' else 0
        for b in brackets[1:]:
            if b == '(':
                opening += 1
            else:
                opening -= 1
            out.append(opening)
        return out
    
    if len(lst) != 2:
        return "Invalid input"
    
    brackets_a = lst[0]
    brackets_b = lst[1]
    
    shifted_a = shift_brackets(brackets_a.split(")"))
    shifted_b = shift_brackets(brackets_b.split("("))
    
    if max(shifted_a) != max(shifted_b):
        return "No"
    
    return "Yes"
```

The approach revolves around the fact that a string of parentheses can be considered "balanced" or "good" if it is possible to traverse it using a stack data structure, such that at any point the number of opening parentheses on the stack is greater than or equal to the number of closing parentheses.

Shift the opening/closing parentheses into a list of numbers, where an opening parentheses corresponds to 1 and a closing parentheses corresponds to 0. Then, the maximum value in this list corresponds to the maximum number of opening parentheses we have at any point. If this maximum is larger for one of the shifted strings, then it's impossible to balance the parentheses. Otherwise, there's a way to concatenate the strings in some order and maintain a balanced parentheses.