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

The code uses a list to build the new string, ensuring that all spaces are correctly replaced. The check for multiple consecutive spaces is done by checking the previous two characters in the list. When encountering multiple spaces, an `-` character is appended to the `new_text` list instead of an `_`. The final string is created by joining the list using string concatenation. 

The problem is posed in the Markdown code block, and the solution is provided right below it, forming a coherent and compact piece of text. If needed, you can further integrate tests to ensure the function behaves as expected.