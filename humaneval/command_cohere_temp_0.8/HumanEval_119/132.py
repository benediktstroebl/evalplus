```python
def match_parens(lst):
    def shift(s):
        """
        Shifts the parentheses in S in an optimal way
        so that the result will be balanced.
        """
        if not balance[s]:
            return False
        stack, rev_stack = [], []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                rev_stack.append(c)
        stack.reverse()
        return stack + rev_stack[::-1]

    def calc(s1, s2):
        """
        Calculates the balance of the concatenation of two strings.
        """
        s = s1 + s2
        balance[s] = calc_balance(s)
        return balance[s]

    def calc_balance(s):
        """
        Calculates the balance of a string.
        A string S is considered to be balanced
        if the number of open parentheses '(' is equal to the number of close parentheses ')'
        """
        balance[s] = (s.count('(') == s.count(')'))
        return balance[s]

    balance = {}
    if len(lst) != 2:
        return 'No'
    s1, s2 = lst
    if not shift(s1) or not shift(s2):
        return 'No'
    if calc(s1, s2) or calc(s2, s1):
        return 'Yes'
    else:
        return 'No'
```

The solution is based on the following ideas:
1. If we can shift the parentheses in one string in an optimal way
   so that the result will be balanced, then we can concatenate
   the two strings in any order and the result will be balanced.
2. If we can't shift the parentheses in one string, then the concatenation
   of these two strings will always be unbalanced. 

The function shift works with one string at a time. It tries to balance
the string using a stack (simulating the shifting of parentheses).
The function calc calculates the balance of the concatenation
of two strings using the calc_balance function.
The main function just checks if it's possible to apply shift to both strings
and if the result of the concatenation of these shifted strings is balanced.