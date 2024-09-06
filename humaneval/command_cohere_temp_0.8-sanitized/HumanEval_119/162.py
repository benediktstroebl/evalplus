def match_parens(lst):
    def check(s, br):
        if len(s) == len(br):
            return all(si == '(' == bri or si == ')' == bri for si, bri in zip(s, br))
        return False
    return 'Yes' if any(check(s, br) for s, br in zip(lst, lst[1:])) else 'No'