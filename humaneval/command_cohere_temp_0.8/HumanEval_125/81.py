```python
import re

def split_words(txt):
    if re.search(r'\s', txt): 
        return txt.split()
    elif re.search(r',', txt): 
        return txt.split(',')
    else: 
        return len(list(filter(lambda x: ord(x) % 2 == 0, txt)))
``` 

The problem defines the following conditions to help determine the behavior of the `split_words` function:
1. If the input `txt` contains at least one whitespace character (` ' ', '\t', '\n', '\r', '\f', etc.), the function should split `txt` into a list of words, where each word is a substring separated by whitespace. This is achieved using the `re.search()` function to check for the presence of any whitespace and then splitting the text using the `split()` method.
2. If the input `txt` does not contain any whitespace but contains at least one comma (`,`), the function should split `txt` into a list of words, where each word is a substring separated by commas. This is achieved by checking for the presence of commas using `re.search()` and then splitting the text using the `split()` method with `,` as the separator.
3. If the input `txt` does not contain any whitespace or commas, the function should return the total count of lowercase letters with an odd numeric value when interpreted as an integer. To achieve this, the function uses a list comprehension and the `filter()` function to filter out all lowercase letters with an even ASCII value (odd parity), and then calculates the length of this filtered list.

The provided code uses the `re` module to perform the regular expression searches efficiently, and the conditional structure to determine the appropriate splitting behavior or odd letter count calculation.

Keep in mind that the behavior of this function assumes that the input text is a string of words without any enclosing punctuation, and the output is expected to be a list of words if splitting is applicable, or an integer if counting odd letters applies. 

This solution assumes all words in the input are composed of lowercase letters. If the problem allows for uppercase letters or other characters, additional modifications would be necessary.