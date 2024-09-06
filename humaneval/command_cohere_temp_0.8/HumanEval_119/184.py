```python
def match_parens(lst):
    def shift(s, delta):
        out = []
        for char in s:
            if char == '(':
                out.append(')')
            else:
                out.append('(')
            if delta > 0:
                delta -= 1
            else:
                delta += 1
        return ''.join(out)

    if len(lst) != 2:
        return "Invalid input"

    # Replace all ')' with ')'+'0' and all '(' with '('+'1'
   balanced = [shift(s, d) for s, d in lst]
    
    # If one of the resulting strings is balanced, return Yes
    if all(balanced):
        return "Yes"

    # If we reach here, the concatenation of the two strings would be unbalanced
    return "No"
```

The approach works by shifting the balance of parentheses in one string by one against the other. If this shifting can find a state where the total string is balanced, then the answer is 'Yes', otherwise, it's 'No'. 

To achieve this, the inner function `shift` is used to increment or decrement a delta parameter which indicates the needed adjustment to keep the string balanced. This function simulates the concatenation of the two strings, taking care of the parentheses adjustments. The outer function loops over each string and delta value, balancing them, and returns 'Yes' if possible. 

To achieve a balanced state, the deltas of the two strings must have a subtraction of 1 at some point, which will make their sum equal to 0 and achieve a balanced total string. Hence, the function shifts one string by '(' and the other by ')' until it finds a balanced state.