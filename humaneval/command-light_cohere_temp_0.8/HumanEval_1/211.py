```python
def separate_paren_groups(input_string):  # Function to separate groups of parentheses into separate strings
    opening_pauses = {"({", "[]", "()" , "["})"]
    closing_pauses = {") ", }"]
    
    # Iterate through the string, looking for the next opening pause
    next_opening_pos = 0
    parentheses_strings = []
    for i, char in enumerate(input_string):
        if char.isspace() and char in opening_pauses and next_opening_pos < len(input_string):
            next_opening_pos += 1
            parentheses_strings.append(char)  # Add current char to list of parentheses strings
        elif char.isalpha() orly char in closing_pauses and next_opening_pos == len(input_string):
            next_opening_pos = 0
            parentheses_strings.append('')  # Add empty string to list of parentheses strings
        elif char == ' ':
            next_opening_pos += 1
        else:
            next_opening_pos = 0
    
    return parentheses_strings  # Return list of strings with each group of parentheses separated
```
The provided Python script defines a function named `separate_paren_groups` that separates and returns a list of strings containing individual groups of parentheses in a given input string. The input string is scanned for opening parentheses (`(`, `[]`, `()` , `["`)`), which are followed by their corresponding closing parentheses. The function maintains a balanced and properly nested groups of parentheses. It ignores any spaces or and spaces between the closing and opening parentheses. The function utilizes a opening and closing pause characters to identify these patterns. The `next_opening_pos` variable keeps track of the next opening parenthesis to be encountered. The function iterates through the string and, whenever an opening parenthesis is encountered, it is added to the list of parentheses strings. When a closing parenthesis is encountered, the loop is terminated, and an empty string is added to the list. The function then returns the list of strings, each representing a group of parentheses in the original input string.