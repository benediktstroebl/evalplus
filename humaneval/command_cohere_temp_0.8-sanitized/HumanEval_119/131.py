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