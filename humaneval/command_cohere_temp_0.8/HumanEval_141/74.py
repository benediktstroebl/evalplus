```python
def file_name_check(file_name):
    lat_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_dot = 0
    act_sub = file_name.split('.')

    if len(act_sub[0]) == 0 or (act_sub[0][0] not in lat_alphabet):
        return "No"
    else:
        if len(act_sub[0]) > 3: 
            return "No"
        
        if file_name.endswith('.txt') or file_name.endswith('.exe') or file_name.endswith('.dll'):
            return "Yes"
        else:
            return "No"
```

The function checks the file name according to the problem's statement. The function splits the file name into its prefix and suffix using the dot as a delimiter. The prefix cannot be an empty string or start with a digit. The suffix must be one of the specified extensions. 

The function returns "Yes" if all conditions are met, and "No" otherwise. You can test this function by calling it with different file names and verifying that it returns the correct results based on the conditions specified in the problem statement.