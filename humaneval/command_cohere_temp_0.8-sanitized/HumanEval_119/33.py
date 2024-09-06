def match_parens(lst):
    def shift_left(s):
        return s[:len(s) - len(re.sub(r'(\))+', r' \1', s))]

    return 'Yes' if all(shift_left(s) == s for s in lst) else 'No'