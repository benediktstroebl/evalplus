def match_parens(lst):
    def shift(s, offset):
        out = []
        for char in s:
            if char == '(':
                out.append(')' if offset else '(')
            else:
                out.append(char)
        return ''.join(out)

    return 'Yes' if max(map(shift, lst, [1, -1])) == ')' else 'No'