# CANNOT PARSE CODE SNIPPET
def correct_bracketing(brackets: str) -> bool:
    count = 0
    for bracket in brackets:
        if bracket == "<":
            count += 1
        elif bracket == ">":
            count -= 1
            if count < 0:
                return False
    return count == 0
