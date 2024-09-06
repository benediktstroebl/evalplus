def correct_bracketing(brackets):
    open_brackets = len(brackets) - brackets.count('(')
    close_brackets = len(brackets) - brackets.count(')')
    return open_brackets == close_brackets