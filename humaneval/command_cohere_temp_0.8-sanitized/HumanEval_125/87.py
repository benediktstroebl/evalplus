import re
def split_words(txt):
    # split on whitespace if it exists
    try:
        return re.findall(r'\w+', txt.strip())
    except AttributeError:
        pass
    # If no whitespace, split on commas
    return re.findall(r'\w+,\w+', txt.strip())