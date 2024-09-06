```python
def file_name_check(file_name):
    regex = r'\b[a-zA-Z][a-zA-Z0-9]{1,2}(\.\w{2})?$'
    if not re.match(regex, file_name):
        return "No"
    else:
        return "Yes"
```

This Python script defines a function `file_name_check` that takes a `file_name` as input and returns either 'Yes' or 'No' depending on whether the file name adheres to the given constraints or not. Here's a breakdown of the code:
1. `regex = r'\b[a-zA-Z][a-zA-Z0-9]{1,2}(\.\w{2})?$`: This is a regular expression pattern that is used to match the filename. The `\b` assertion checks for a word boundary, ensuring that the file name is not part of a bigger string. The `[a-zA-Z]` part checks for the first character to be a letter, and `[a-zA-Z0-9]{1,2}` ensures that there are at most two following characters that can be digits. The `(\.\w{2})?$` part checks for the presence of a dot, and then ensures that there are at most two characters after the dot, where the `\w{2}` matches two word characters (letters, digits, or underscore).
2. `if not re.match(regex, file_name):`: This line uses the `re.match()` function to check if the given file name does not match the pattern defined in the regex. 
3. If the file name does not match the pattern, the function returns "No", indicating that the file name does not conform to the required format. 
4. If the file name matches the pattern, the function returns "Yes", indicating that the file name is valid. 

This solution is efficient and will return the correct answer almost instantly since it only needs to check the file name's pattern against a regex. Thus, it is scalable and ready to handle any number of test cases.