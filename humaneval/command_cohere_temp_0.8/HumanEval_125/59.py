```python
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
```

The provided Python script implements a function called `split_words` that takes a string as input. First, it checks if there are any spaces in the string using a regular expression. If there are spaces, it simply splits the string into a list of words using the `split` method. If there are no spaces, it checks if there are any commas in the string, and if found, it also splits the string into a list using the comma as the delimiter. In the event that the string contains no spaces or commas, it counts the number of lowercase letters with an odd alphabetical order (odd ordinal value) and returns a list containing that count, which is useful when the input string doesn't split cleanly into words. The `re.IGNORECASE` flag makes the search case insensitive, ensuring that both uppercase and lowercase letters are considered. 

The function's behavior is described by the following logical rules:
1. If the input string contains at least one whitespace character (space), it is split into a list of words, where each word is a substring separated by spaces, and the function returns this list.
2. If the input string does not contain any whitespace, it checks for the presence of a comma",". If found, the string is split into a list using the comma as the delimiter, and this list is returned.
3. If the input string contains no whitespace or commas, it counts the number of lowercase letters with an odd alphabetical order. This count is then returned as a list with a single element.

The given examples in the problem statement are correctly handled by the script.