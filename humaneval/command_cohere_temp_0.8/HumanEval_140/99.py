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

The code uses a for loop to iterate over each character in the `text` string. When a space is encountered, the code checks the previous two characters to see if they are both spaces. If so, it replaces the space with a `-` to avoid having too many consecutive spaces. If the two previous characters are not both spaces, it simply replaces the space with an underscore. 

The code fragment does not utilize any third-party libraries and should work in any Python environment. It can be easily incorporated into larger projects as well as ran standalone for testing.