def match_parens(lst):
    def shift(s):
        """
        Shifts the parentheses in S in a way that if concatenated with the
        other string, will result in a well-formed parentheses sequence.
        """
        if not s:
            return s
        balance = 0
        shifted = []
        for i, char in enumerate(s):
            if char == '(':
                balance += 1
                if balance == 0:
                    shifted.append(')')
            else:
                balance -= 1
                if balance == 0:
                    shifted.append('(')
        return shifted

    return 'Yes' if len(set(shift(s) for s in lst)) == 1 else 'No'