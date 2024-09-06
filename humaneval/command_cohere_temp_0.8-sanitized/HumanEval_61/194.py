def correct_bracketing(brackets):
    try:
        num_brackets = len(brackets.split(')'))
        if num_brackets != len(brackets.split('(')):
            return False
        return all(a == b for a, b in zip(brackets.split('('), brackets.split(')')))
    except ValueError:
        return False