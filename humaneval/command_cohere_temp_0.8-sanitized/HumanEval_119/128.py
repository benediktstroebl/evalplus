def match_parens(lst):
    def shift(s):
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            else:
                cnt -= 1
            yield from ([char] * cnt)

    return 'Yes' if all(shift(s)[-1] == ')' for s in lst) else 'No'