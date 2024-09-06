```python
def match_parens(lst):
    # Use a counter to keep track of opening parentheses
    counter = 0

    for char in lst[0] + lst[1]:
        if char == '(':
            counter += 1
        else:
            counter -= 1

        if counter < 0:  # Unbalanced
            return "No"

    return "Yes"
``` 

The function evaluates the balance of parentheses in the two strings using a counter to count the opening parentheses '(' and subtracts the closing parentheses ')' to check for balance. If the total count of opening parentheses is less than the total count of closing parentheses at any point, the function returns "No" since the strings are not suitable for concatenation to form a balanced parentheses string. Otherwise, it returns "Yes" if it is possible to form a balanced string by concatenating the two strings in any order.