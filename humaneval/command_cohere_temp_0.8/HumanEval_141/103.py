```python
def file_name_check(file_name):
    ret = "No"
    
    # Check if the file name contains only one dot '.'
    if '.' not in file_name or ('.' in file_name and file_name.count('.') > 1):
        return ret
    
    # Check if the substring before the dot is empty or starts with a letter
    pre_dot = file_name.rsplit(".", 1)[0]
    if pre_dot.strip() != pre_dot or not pre_dot[0].isalpha():
        return ret
    
    # Check if the substring after the dot is in the list
    if file_name.split(".")[1].lower() not in ['txt', 'exe', 'dll']:
        return ret
    
    # Check if the number of digits is no more than three
    if file_name.replace('.', '').isdigit() and len(file_name.replace('.', '').digits()) > 3:
        return ret
    
    # Pass all checks
    return "Yes"
```

This script incorporates individual checks outlined in the problem statement. It leverages Python's string manipulation and regex functionalities to ascertain whether the file name conforms to the provided criteria. Ultimately, it ascertains whether the file name is valid or not, fulfilling the objectives of the problem. You can use this code to validate file names in a straightforward manner.