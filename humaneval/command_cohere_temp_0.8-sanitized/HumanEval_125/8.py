import re
def split_words(txt):
    # split on whitespace if present
    try:
        return re.findall(r'\w+', txt)
    except:
        pass
    
    # split on commas if no whitespace
    try:
        return re.findall(r'\w+,\w+', txt)
    except:
        pass
    
    # return the number of lower-case letters with odd order in the alphabet
    return len([char for char in txt if ord(char) % 2 == 1 and char.islower()])