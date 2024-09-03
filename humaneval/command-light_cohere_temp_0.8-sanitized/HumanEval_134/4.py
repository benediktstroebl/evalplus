def check_if_last_char_is_a_letter(txt):
    # Remove all non-alphatic letters and spaces from the string
    txt = txt.replace(str.maketrans(' ', 'a'))
    # Return True if the last character is an alphabetical character and is not a part of a word
    return txt[-1].isalpha() and not txt.isspace()