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