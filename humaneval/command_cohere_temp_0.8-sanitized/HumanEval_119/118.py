def match_parens(lst):
    def shift(s):
        if not balance[s]:
            return False
        balance[s] -= 1
        return True

    def pop(s):
        if not balance[s]:
            return False
        balance[s] -= 1
        return True