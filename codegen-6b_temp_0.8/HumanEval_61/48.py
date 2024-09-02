

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    info = {}
    for i,c in enumerate(brackets):
        if c not in info:
            info[c] = {'open':[i], 'close':[]}
        else:
            if c+1 not in info:
                info[c+1] = {'open':[i], 'close':[]}
            info[c]['open'] += info[c+1]['open']
            info[c]['close'] += info[c+1]['close']
            del info[c+1]
    for k,v in info.items():
        if k != '(' and k != ')':
            if len(v['open']) > 1:
                return False
    return True

