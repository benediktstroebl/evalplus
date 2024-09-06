```python
def file_name_check(file_name):
    Checks = [lambda: len(set(char for char in file_name if char.isdigit())) <= 3, 
             lambda: '.' in file_name, 
             lambda: file_name.split(".")[0][0].isalpha(), 
             lambda: file_name.split(".")[1] in ['txt', 'exe', 'dll']]
    return "Yes" if all(Check() for Check in Checks) else "No"
```

The script employs a list of lambda functions to validate various conditions related to file naming. It then employs the `all()` function to evaluate if all conditions have been met. If so, the function returns "Yes," and if not, it returns "No." This approach allows for concise, structured condition checking within the script.

To perform each individual check the lambda functions employ different regex and string methods, such as:
- `len(set(char for char in file_name if char.isdigit())) <= 3` : uses a generator expression to extract only digits from file_name and then creates a set to eliminate duplicates, finally checking the size of this set against a maximum of 3.
- `'.' in file_name`: uses the in operator to search for the dot "."; 
- `file_name.split(".")[0][0].isalpha()`: uses the split method to divide the file name into a list, accesses the first element of this list ([0]) and then accesses the first character (0) to check if it is alphabetic;
- `file_name.split(".")[1] in ['txt', 'exe', 'dll']`: uses the split method to divide the file name into a list, accesses the second element of this list ([1]) and checks if the string is in the provided list. 

This approach allows the script to efficiently evaluate file name validity based on several conditions.