def correct_bracketing(brackets):
    open_brackets = len(brackets.split('('))
    close_brackets = len(brackets.split(')'))
    return open_brackets == close_brackets