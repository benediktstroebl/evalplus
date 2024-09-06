```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The Python script fixes spaces in the given string and provides different behaviors for a single space and multiple consecutive spaces. You can test this function with the provided test cases to ensure it behaves as expected. Let's explain this code for better understanding:
1. The `fix_spaces` function takes a single argument `text`, which is the input string that contains spaces to be replaced. 
2. This function iterates through each character of the input string `text` using a `for` loop.
3. Inside the loop, it checks if the character is a space character using an `if` statement.
4. If the character is a space, it means that the `new_text` list (which is initially an empty list) could contain consecutive spaces, and the length of `new_text` matters.
5. The conditional `if len(new_text) > 1 && new_text[-1] == ' '` checks whether the last character added to `new_text` is a space. If it is, the function replaces the consecutive spaces with a single - (hyphen). This is done to ensure only single spaces are replaced, and consecutive spaces are collectively replaced with a hyphen.
6. If the character is not a space, it is added to the `new_text` list as is, meaning non-space characters are unchanged.
7. After processing all characters in the string, the function joins the `new_text` list back into a string, assuming the rest of the string is a string, and returns the result. 

This approach ensures that single spaces are replaced with underscores and consecutive spaces are replaced with hyphens, as described in the problem statement.