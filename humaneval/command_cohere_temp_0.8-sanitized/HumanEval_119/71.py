def match_parens(lst):
    opened = lst[0]
    closed = lst[1]
    if len(opened) + len(closed) == 0:
        return "Yes"
    diff = [x for x in opened if not x in closed]
    if diff:
        return "No"
    return match_parens([x for x in opened if x in closed], [x for x in closed if x in opened])