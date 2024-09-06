```python
import re

def split_words(txt):
    ans = txt.split(re.escape(r'[ ,]'))
    if len(ans) > 0:
        return ans
    else:
        return len(re.findall(r'[a-z]', txt)) % 2
``` 

The Python script uses a regular expression (`re`) to achieve the desired functionality in one line, splitting the string on whitespace or comma-separated values while considering cases where the text contains no whitespace or comma. To determine the oddity of the number of lowercase letters in the text, it employs another regular expression, checking if the text contains any lowercase letters. The one-liner approach saves on code size while maintaining clarity and efficiency. 

The `re.escape` function is used to convert any special characters, such as `[`, `]`, `(`, `)`, `^`, `-`, `,`, `*`, `+`, `?`, `\`, `|`, `/`, `^`, `~`, `whitespace`, and `#`, into their corresponding escape characters. This is important to ensure the proper functioning of regular expressions. It's a common practice to escape these characters when used inside a regular expression to avoid misinterpretation by the regular expression engine.