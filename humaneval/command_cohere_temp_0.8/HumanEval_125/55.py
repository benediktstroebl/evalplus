```python
import re

def split_words(txt):
    """
    Split the given string of words into a list, taking into account whitespace and commas.
    If no such separators exist, return the count of lowercase letters with odd alphabetical order.
    """
    if re.match(r'^[a-z]+$', txt, re.IGNORECASE): 
        return len(txt) if sum(1 for _ in txt if _ in '02468') % 2 == 1 else 0
    return re.split(r'\s*,\s*|\s+', txt)
``` 

The solution leverages regular expressions ([a-z]+)$ to check if the text is composed of lowercase letters only. The re.IGNORECASE flag ensures the check is case-insensitive. If the condition is met, it returns the total count of letters if the sum of occurrences of letters with odd alphabetical order is odd, and 0 otherwise. If the text is not a string of lowercase letters, the re.split() function is used to split the string into a list based on whitespace and commas.

The regular expression (\s*,\s*|\s+) captures either a comma followed by zero or more whitespace characters, or one or more whitespace characters. This takes care of splitting the string on whitespace or comma.

To handle the odd letter count condition, the sum(1 for _ in txt if _ in '02468') snippet checks for the count of letters with odd order in the alphabet. Let's break it down:
- The underscore _ is used as a placeholder in the generator expression.
- The generator expression in sum(...) iterates over each character in the text txt.
- The character is checked if it is in '02468', which are the letters of the English alphabet with odd alphabetical order.

The condition therefore checks if the number of letters with odd alphabetical order is odd, as requested in the prompt. 

Keep in mind that the order of letters in the English alphabet is odd, so 'a' has an odd position, but 'b' has an even position, and so on. The letter 'z' has an odd position, which is 25.