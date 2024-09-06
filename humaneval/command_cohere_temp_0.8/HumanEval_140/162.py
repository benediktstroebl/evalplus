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

The code uses a for loop to iterate through each character in the input `text`, if the character is a space, it checks the previous two characters to see if they are both spaces, and if so, it replaces the space with a -, otherwise, it replaces the space with an _. The resulting string is then returned. 

To run this code, you can import it into a Python script and call the `fix_spaces()` function with different input strings to check the result. 

Let me know if you would like to know more about the problem or the solution!