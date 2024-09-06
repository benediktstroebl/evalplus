import re
def split_words(txt):
    """
    Split the input text into words, handling various separators.
    If no separators are found, return the count of lowercase letters with odd alphabetic ordinals.
    """
    if re.match(r'[a-z]+', txt):      # No separators found, count odd alphabetic ordinals
        return len(txt) - sum(ord(c)%2 == 0 for c in txt)
    elif re.search(r'\W', txt):     # Non-alphanumeric characters present, split by spaces
      return txt.split()
    else:                           # Otherwise, split by commas
      return re.split(r'\,', txt)