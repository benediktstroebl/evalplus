```python
import re

def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you should 
    split on commas ',', if no commas exists you should return the number of lower-case letters with odd order in the 
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
   Examples
    split_words("Hello world!") → ["Hello", "world!"]
    split_words("Hello, world!") → ["Hello", "world!"]
    split_words("abcdef") → 3 
    """
    # use regex to split on whitespace or comma if they are surrounded by a letter, digit, or underscore
    # this ensures that the delimiter is not considered a part of the word
    txt = re.sub(r'([a-z0-9_]+)([ ,]+)([a-z0-9_]+)', r'\1\3', txt)
    # if after removing commas and whitespaces from the text we are left with a single word, return the number of letters with odd order in the alphabet 
    if txt.isalpha(): return len(txt) if sum(1 for _ in txt if _.islower()) % 2 == 1 else 0
    # if we have more than one word in the text after removing commas and whitespaces, return the list of words
    return txt.split(',') if ',' in txt else ['OK'] # return ['OK'] if there are no commas or whitespaces to ensure the function returns a list
```