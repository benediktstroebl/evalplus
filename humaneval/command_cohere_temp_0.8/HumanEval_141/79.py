```python
def file_name_check(file_name):
    checker = lambda s: len(s) <= 1 and s[0] in '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    num_digits = sum(1 for c in file_name if c in '0123456789')
    has_dot = '.' in file_name
    substring_before_dot, file_extension = file_name.split('.')[:2]
    
    passes_letter_check = checker(substring_before_dot) and checker(file_extension)
    
    valid_extensions = ['txt', 'exe', 'dll']
    passes_extension_check = file_extension in valid_extensions
    
    if num_digits <= 1 and has_dot and passes_letter_check and passes_extension_check:
        return "Yes"
    else:
        return "No"
```

The function directly evaluates the conditions required by the prompt and returns 'Yes' or 'No' accordingly. Let's break down the function step-by-step:
1. **Checker Function**: The lambda function `checker` is meant to check if a given string `s` conforms to the rule that its length should be <= 1, and the first character should be a letter or a dot. This is used to validate the filename substring before the dot and the file extension.
2. **NumberOfDigits**: This counts the number of digits in the `file_name`. If there are more than three digits, it fails the condition stated in the prompt.
3. **HasDotSubstring**: This checks if the `file_name` contains a dot using standard string manipulation methods in Python.
4. **SplitFilename**: The `file_name` is split at the dot using `split('.')`, which returns a list with two elements: the substring before the dot and the file extension. These are extracted and stored in the `substring_before_dot` and `file_extension` variables.
5. **PassesLetterCheck**: Both the `substring_before_dot` and `file_extension` are passed through the `checker` lambda function. If the lambda returns True for both, it passes this condition.
6. **PassesExtensionCheck**: A list of valid file extensions is hardcoded (`valid_extensions = ['txt', 'exe', 'dll']`) and the `file_extension` is checked against this list. If the extension is valid, it passes this condition.

Finally, the function evaluates all these conditions and returns 'Yes' if the file name is valid and 'No' otherwise.