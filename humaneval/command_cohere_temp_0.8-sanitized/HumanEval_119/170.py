def match_parens(lst):
    def shift(ss):
        """
        Shifts the string ss by incrementing all '(' and decrementing all ')' until balanced
        :param ss: string to shift
        :return: balanced string
        """
        delta = 0
        while len(ss) != 0 and ss[-1] != '(':
            if ss[-1] == ')':
                delta += 1
            ss = ss[:-1]
        while delta != 0:
            if delta > 0:
                ss += ')'
                delta -= 1
            else:
                ss += '('
                delta += 1
        return ss
    
    if len(lst) != 2:
        return "Invalid Input"
    s1, s2 = lst
    if s1 == s2:
        return "No"
    if len(s1) == 1 and len(s2) == 1:
        return "Yes"
    return "No" if shift(s1 + s2) == ')' or shift(s2 + s1) == ')' else "Yes"