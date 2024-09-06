```python
def file_name_check(file_name):
    dots = file_name.count('.')
    if dots != 1:
        return "No"
    pre, ext = file_name.split('.')
    if len(pre) == 0 or not pre[0].isalpha():
        return "No"
    if len(ext) > 3 or ''.join(ext) not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
```

The code divides the given file name into its prefix (everything before the first dot) and the extension (everything after the first dot). It then checks if the dot exists exactly once, the prefix is not empty and starts with a letter, and the extension is "txt", "exe", or "dll" and is no more than 3 characters long.