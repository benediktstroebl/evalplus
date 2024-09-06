def match_parens(lst):
    close = ')'
    for open in lst:
        if open != close:
            balance = 0
            s = open + close
            while s:
                if s.count(open) > s.count(close):
                    return "No"
                balance += s.count(open) - s.count(close)
                s = s[:-1]
            if balance == 0:
                return "Yes"
    return "No"