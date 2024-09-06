```python
def match_parens(lst):
    def shift(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return True

    return 'Yes' if shift(lst[0] + lst[1]) else 'No'
``` 

The provided Python script solves the problem of checking if two strings consisting of parentheses can be concatenated to form a balanced string. The inner function `shift` keeps track of the balance of parentheses as it iterates through the characters of a string. If at any point the balance goes negative, indicating an unbalanced string, the function returns False. Otherwise, it returns True. The outer function `match_parns` simply combines the two input strings and checks if they can form a balanced string when shifted, using the inner function. Thus, the function returns 'Yes' if it is possible and 'No' otherwise.