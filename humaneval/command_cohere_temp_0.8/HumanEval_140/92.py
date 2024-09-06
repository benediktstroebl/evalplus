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

The function iterates through the input text, and for each character, it checks if the character is a space. If the character is a space, the function checks the previous character in the text (to check if the previous text ended with '-', thereby avoiding overwriting it with an underscore). If the previous character is not an '-', it replaces the space with an underscore, otherwise, it keeps the space. 

This solution is efficient and can solve the given problem in `O(n)` time, where `n` is the number of characters in the string. And it is also concise and easy to understand, which is a benefit when it comes to maintaining and rewriting the code. 

This script solves the problem statement in a precise and straightforward way. It does not attempt to over-optimize the solution, making it a reliable option in this given context.