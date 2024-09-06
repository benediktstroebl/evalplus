def match_parens(lst):
    def shift(s):
        ret = []
        left = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                ret.append(left)
                left -= 1
        if left != 0:
            return False
        return ret
    
    if len(lst) != 2:
        return "Invalid input"
    
    # reverse the second string
    lst.append(shift(lst.pop()))
    
    # stack all sequences and see if they are equal
    stack = [shift(s) for s in lst]
    if stack[0] != stack[1]:
        return "No"
    
    return "Yes"