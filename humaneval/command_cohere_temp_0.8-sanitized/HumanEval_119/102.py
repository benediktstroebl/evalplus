def match_parens(lst):
    def count(s):
        return sum(1 for char in s if char == '(')

    if lst[0] == lst[1]:
        return "Yes" if count(lst[0]) % 2 == 0 else "No"
    elif lst[0][-1] == lst[1][0]:
        return "Yes" if count(lst[0]) % 2 == 0 else "No"
    elif lst[0][0] == lst[1][-1]:
        return "Yes" if count(lst[1]) % 2 == 0 else "No"
    else:
        return "No"