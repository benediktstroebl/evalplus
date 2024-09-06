
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

    def _replace(s):
        res = []
        for c in s:
            if c != ' ':
                res.append(c)
            else:
                if len(res) == 0:
                    res.append('_')
                elif len(res) == 1:
                    res.append('-')
                else:
                    res.append('_')
        return ''.join(res)
    return _replace(text)

