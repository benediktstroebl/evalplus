
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
    def replace_consecutive_spaces(text):
        """
        Replace all consecutive spaces with -
        """
        return text.replace(" ", "-")
    
    def replace_one_or_two_spaces(text):
        """
        Replace one or two spaces with _
        """
        spaces = 0
        for char in text:
            if char == " ":
                spaces += 1
                if spaces == 1:
                    continue
            else:
                break
        return "_" * spaces
    
    return "".join(map(lambda x: replace_consecutive_spaces(x) if len(x) > 2 else replace_one_or_two_spaces(x), text.split(" ")))
