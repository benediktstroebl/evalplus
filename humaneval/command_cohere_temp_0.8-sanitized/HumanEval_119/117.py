def match_parens(lst):
    def shift(s):
        ret = []
        for i in s:
            if i == '(':
                ret.append(i)
            else:
                ret.append(')')
        return ''.join(ret)

    return 'Yes' if shift(lst[0]) == shift(lst[1]) else 'No'