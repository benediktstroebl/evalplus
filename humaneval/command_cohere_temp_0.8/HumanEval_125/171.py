```python
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
```

The solution leverages regular expressions (`re` module) to achieve this in a concise and efficient manner.

Here's an breakdown of the script:

1.  The `re.match(r'[a-z]+', txt)` checks if the input text consists entirely of lowercase letters. If it is, the function proceeds to count the number of lowercase letters with odd alphabetic ordinals and returns the result.
2.  The `re.search(r'\W', txt)` checks if there are non-alphanumeric characters (e.g., spaces) in the text. If found, the function splits the text into a list of words using spaces as separators.
3.  Otherwise, if no spaces are found, the function uses `re.split(r'\,', txt)` to split the text into a list of words using commas as separators.

The regular expressions used in this code are powerful and versatile, allowing the function to handle various input scenarios while providing a concise and efficient solution to the problem.