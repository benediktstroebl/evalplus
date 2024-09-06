import re
def split_words(txt):
    """
    Split the given string of words into a list, taking into account whitespace and commas.
    If no such separators exist, return the count of lowercase letters with odd alphabetical order.
    """
    if re.match(r'^[a-z]+$', txt, re.IGNORECASE): 
        return len(txt) if sum(1 for _ in txt if _ in '02468') % 2 == 1 else 0
    return re.split(r'\s*,\s*|\s+', txt)