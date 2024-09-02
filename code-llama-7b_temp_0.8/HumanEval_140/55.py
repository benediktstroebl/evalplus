
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

    # if there is not a space
    if " " not in text:
        return text

    # if there is a space
    else:
        # split on space
        split_text = text.split(" ")

        # go through each element
        for i in range(len(split_text)):
            # if the element is longer than 1
            if len(split_text[i]) > 1:
                # replace the element with the underscore version
                split_text[i] = split_text[i].replace(" ", "_")

        # replace the text with the fixed text
        text = " ".join(split_text)
        return text
