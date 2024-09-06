```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) == 0 or new_text[-1] != '-':
                new_text.append('_')
            else:
                new_text.append(c)
        else:
            new_text.append(c)
    return ''.join(new_text)
```

The code uses a list to build the new string, ensuring that consecutive spaces are replaced with '-' only when the previous character is not an underscore. It also utilizes a join function to transform the list into a string. You can test it by calling the function with different input strings as shown in the original problem statement. Feel free to ask any questions or raise concerns; I aim to provide clear and useful responses. Please let me know if you'd like further clarification or additional explanations.