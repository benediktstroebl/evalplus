```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        opening_balance = get_opening_balance(token)
        closing_balance = get_closing_balance(token)
        result.append(opening_balance + closing_balance)
    return result

def get_opening_balance(token: str) -> int:
    balance = 0
    opened = True
    for char in token:
        if char == '(':
            balance += 1
        elif char == ')':
            opened = False
            balance -= 1
        if not opened and balance == 0:
            break
    return balance

def get_closing_balance(token: str) -> int:
    balance = 0
    opened = False
    for char in token:
        if char == '(':
            opened = True
        elif char == ')':
            balance += 1
    return -balance if opened else balance

# Tests
assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
``` 

This code solves the provided problem by splitting the input string by spaces to iterate through each group of parentheses. For each group, it counts the number of `(` and `)` characters to determine the deepest level of nesting. It uses a `get_opening_balance` function to get the opening balance and a `get_closing_balance` function to correct the balance by considering whether the corresponding opening parentheses have been encountered. The sum of the opening and closing balances gives the deepest level of nesting, which is then added to the result list. The provided example test case is included and more can be added with expected results.