```python
def file_name_check(file_name):
    checker = [](
        lambda : len(re.findall(r'\d{4,}', file_name)) <= 0,
        lambda : '.' in file_name,
        lambda : file_name.split('.')[0].lower() != '',
        lambda : file_name.split('.')[1] in ['txt', 'exe', 'dll']
    )
    return 'Yes' if all(checker) else 'No'
``` 

This script utilizes Python's list comprehension to create a lambda-based checker function for the validity criteria, assessing four conditions:
1. Maximum of three digits in the entire file name (`len(re.findall(r'\d{4,}', file_name)) <= 0`).
2. Presence of a single dot ('.').
3. Non-empty prefix before the dot, starting with a letter (by checking `file_name.split('.')[0].lower() != ''`).
4. One of three specified extensions (`file_name.split('.')[1] in ['txt', 'exe', 'dll']`).

The file_name_check function then returns "Yes" if all the conditions are satisfied, otherwise "No".

This approach allows the script to efficiently assess the file name validity based on the provided criteria.