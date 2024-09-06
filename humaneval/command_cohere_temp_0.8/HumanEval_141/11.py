```python
def file_name_check(file_name):
    lat_let = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    conditions = [
        lambda: len(file_name) > 0,
        lambda: '.' in file_name,
        lambda: file_name.split(".")[0].startswith(lat_let),
        lambda: len(file_name.split(".")[1]) in [1, 2] and file_name.split(".")[1].lower() in ['txt', 'exe', 'dll']
    ]
    
    return "Yes" if all(condition() for condition in conditions) else "No"
```

The function takes the file name as a parameter and checks it against the list of conditions, returning 'Yes' if all conditions are satisfied and 'No' otherwise. You can verify that the function works as expected by calling it with a variety of example file names.