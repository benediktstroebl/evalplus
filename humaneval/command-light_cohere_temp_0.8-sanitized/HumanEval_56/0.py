def correct_bracketing(brackets): 
    """
    Checks if every opening bracket has a corresponding closing bracket in a string of "<" and ">" characters.
    :param brackets: str
    :return: boolean 
    """
    return all(hasClosingBracket(brackets[i:]) for i, bracket in enumerate("<>"))