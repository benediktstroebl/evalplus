def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets