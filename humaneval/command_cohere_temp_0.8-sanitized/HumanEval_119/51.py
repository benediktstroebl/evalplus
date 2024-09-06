def match_parens(lst):
    def check(s, popen, pclose):
        if not popen and not pclose:
            return True
        if popen < pclose:
            # Too many open parentheses
            return False
        while popen:
            if not pclose or popen < pclose:
                return False
            popen -= 1
            pclose -= 1
        return not pclose

    return 'Yes' if any(map(check, lst, lst[1:])) else 'No'