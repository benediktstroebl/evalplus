
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
    # initialize a dictionary to store replacements
    replacements = {
        " ": "_",
        "\t": "_tab_",
        "\r": "_r",
        "\n": "_new_line_"
    }

    # iterate over the string
    for char in text:
        # replace consecutive spaces with -
        if "-" in replacements and char.isdigit():
            # replace consecutive spaces with -
            if replacements["-"] in char:
                char = "".join([replacements.get(c, c) for c in text])
        elif char.isalpha() and len(char.split(" ")) == 2:
            # replace 2 consecutive spaces with -
            char = "_" + char
        else:
            # replace single spaces with _
            char = "_" + char

        # replace any existing underscores with the modified character
        text = text.replace(char, replacements[char])

    return text
