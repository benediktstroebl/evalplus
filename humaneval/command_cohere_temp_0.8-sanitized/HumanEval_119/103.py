def match_parens(lst):
    def shift(s):
        if not balance[s]:
            balance[s] = 1
        else:
            balance[s] += 1
            
    def pop(s):
        if not balance[s]:
            return False
        else:
            balance[s] -= 1
            if not balance[s]:
                del balance[s]
            return True
            
    balance = {}
    for s in lst:
        shift(s)
    for s in lst:
        if all(map(pop, balance)):
            return "Yes"
    return "No"