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

The code uses a for loop to iterate over each character in the input `text`, and uses an empty list `new_text` to store the modified characters. If the character is a space, the code checks the previous two characters to see if they are both spaces, and if so, it appends a hyphen to the end of the list instead of an underscore. If the character is not a space, it is appended as-is to the list. After processing all characters, the function returns the joined string. This solution is efficient and can fix the spaces in a given text as described in the problem statement.