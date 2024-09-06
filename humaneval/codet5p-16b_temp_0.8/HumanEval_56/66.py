

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """

    
    brackets = brackets.replace("<","&lt;")
    brackets = brackets.replace(">","&gt;")
    brackets = brackets.replace("&lt;","<")
    brackets = brackets.replace("&gt;",">")
    brackets = brackets.replace("&amp;","&")
    
    brackets = brackets.split("<")
    brackets = list(filter(lambda x: x.count("&lt;") < x.count("&gt;"),brackets))
    brackets = [bracket.replace("&lt;","<").replace("&gt;",">") for bracket in brackets]
    
    brackets = list(filter(lambda x: x.count("<") > x.count(">"),brackets))
    
    return len(brackets) == 0
