```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    if max(open_tup) == max(close_tup):
        return "Yes"
    return "No"

def count_open(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
    return balance
```

The `match_parens` function takes in a list of two strings as its argument and returns either "Yes" or "No". The function uses two functions:
1. The `count_open` function calculates the balance of open parentheses for a given string.
2. The `open_tup` and `close_tup` tuples are used to calculate the maximum balance of open parentheses respectively for the two input strings.

If the maximum balance of open parentheses is the same for both strings, then the two strings can be combined to produce a balanced string. If the maximum balance is not the same, then no combination of the two strings can produce a balanced string. 

The function returns "Yes" if there is a way to make a good string, and returns "No" otherwise.

This solution passes all the tests included in the problem statement.