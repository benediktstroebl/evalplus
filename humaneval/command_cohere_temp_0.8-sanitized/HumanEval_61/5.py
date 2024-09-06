def correct_bracketing(brackets):
    open_brackets = len(brackets)
    
    # Counting the number of opening brackets
    brackets = brackets.replace(")", "")
    closed_brackets = open_brackets - len(brackets)
    
    return closed_brackets == open_brackets