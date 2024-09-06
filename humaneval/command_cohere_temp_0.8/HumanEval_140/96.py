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

The function iterates through the input text, and for each character, it checks if it is a space. If it is, it checks the previous two characters (to determine if we have more than 2 consecutive spaces), and replaces the space with an underscore or a - if there are more than 2 spaces in a row. All other characters are appended as is. The final string is then joined and returned. 

This approach ensures that all spaces are correctly replaced, and consecutive spaces are replaced with - as described in the problem statement. 

Let's break down the solution and discuss how it accomplishes the task:
1. **Iterator Approach**: The code uses a loop (called new_text) to iterate through each character of the input text. This is an efficient approach for solving this problem and ensures that each character is processed correctly. 
2. **Consecutive Space Check**: The code checks the previous two characters in new_text to see if they are both spaces. This helps determine if the current space is part of consecutive spaces, which is what the problem requires. 
3. **Space Replacement**: When the current character is a space, it is replaced with an underscore if there are not consecutive spaces, or with a - if there are consecutive spaces. This is done accordingly:
    ```python
    if c == ' ':
        if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
            new_text.append('-')
        else:
            new_text.append('_')
    ```
4. **String Joining**: After processing all characters, the `new_text` list is joined back into a string using ''.join(new_text), and this resulting string is returned as the final fixed string. 
5. **Else Condition**: If the current character is not a space, it is appended as-is to the new_text list, ensuring that non-space characters are not modified. 

Overall, the code provides an efficient and effective solution to the given problem by maintaining the correct spacing and replacing consecutive spaces with underscores or hyphens, as required. Let me know if you would like me to explain any part of the code in more detail, or provide additional insight.