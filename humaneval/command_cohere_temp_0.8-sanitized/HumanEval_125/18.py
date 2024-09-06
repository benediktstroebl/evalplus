import re
def split_words(txt):
    """
    Split the given string of words into a list, optionally splitting on comma if whitespace does not exist.
    If the string contains neither whitespace nor commas, return the count of lowercase letters with odd alphabetical order.
    """
    if re.search(r'\s', txt, re.IGNORECASE): 
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else: 
        alphabetical_oddities = sum(1 for char in txt if ord(char) % 2 == 1 and char.islower())
        return [f"{alphabetical_oddities}"]