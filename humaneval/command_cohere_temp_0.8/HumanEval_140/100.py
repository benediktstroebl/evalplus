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

The Python script fixes spaces in the given string and provides different behaviors for a single space and multiple consecutive spaces. You can test this function with the provided test cases to ensure it behaves as expected. Let's explain this code step by step:

1. **Function Definition**: 
   - The problem defines a function called `fix_spaces(text)` that takes a single argument, `text`.
   - The function proceeds to replace all spaces with either an underscore `_` or a hyphen `-`, depending on the context.

2. **Iterating Over Text Characters**: 
   - The function uses a `for` loop to iterate over each character in the input `text`.
   - Inside the loop, it checks if the character is a space character.

3. **Handling Consecutive Spaces**: 
   - If the character is a space, the function checks if the previous character was also a space (i.e., len(new_text) > 1 and new_text[-1] == ' '). 
   - If this condition is true, it means there are multiple consecutive spaces, and the function replaces them with a single hyphen '-'.
   - If the condition is false, meaning only one space or none, it replaces the space with an underscore `_`.

4. **Building the New Text**: 
   - The function constructs a new string incrementally using the `new_text` list.
   - When the loop finishes iterating over all characters in `text`, the function joins the `new_text` list to form a single string.

5. **Return the Modified String**: 
   - The function returns the modified string, which is the result of the space fixing process. 

This function elegantly handles consecutive spaces by checking the previous character in the new_text list, achieving the desired outcome for the given problem.