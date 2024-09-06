```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The code uses a list (`new_text`) to build the new string, line by line. This is a common technique in Python for creating strings, especially when the string may be constructed in parts. The solution checks beforehand if the next character to be added is a space, and if the previous two characters are also spaces (meaning `new_text` has more than 2 consecutive spaces). If so, it appends a `-` instead of an `_`. Otherwise, it appends an `_`. This technique allows the code to properly handle any number of consecutive spaces. 

The testing process for this function can be made robust by testing a variety of edge cases, including a wide variety of starting strings and different combinations of spaces. The tests should also include valid strings that pass and invalid strings that should throw an error. 

Let me know if you'd like me to expand this answer with some code to test this function!