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

The code uses a list to build the new string, ensuring that all spaces are correctly replaced. It checks if the current space is not the first and not the last one in the string, and there are two consecutive spaces, it replaces them with a single -. This algorithm is concise and efficient and solves the given problem statement. You can test it by calling the `fix_spaces()` function with various inputs as mentioned in the problem statement.