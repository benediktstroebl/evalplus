def match_parens(lst):
    def shift_brackets(brackets):
        out = []
        opening = 1 if brackets[0] == '(' else 0
        for b in brackets[1:]:
            if b == '(':
                opening += 1
            else:
                opening -= 1
            out.append(opening)
        return out
    
    if len(lst) != 2:
        return "Invalid input"
    
    brackets_a = lst[0]
    brackets_b = lst[1]
    
    shifted_a = shift_brackets(brackets_a.split(")"))
    shifted_b = shift_brackets(brackets_b.split("("))
    
    if max(shifted_a) != max(shifted_b):
        return "No"
    
    return "Yes"