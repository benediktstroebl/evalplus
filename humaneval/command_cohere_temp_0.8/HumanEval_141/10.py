```python
def file_name_check(file_name):
    locus, ext = file_name.split('.')
    if len(locus) == 0 or not locus[0].isalpha():
        return "No"
    if len(locus) > 3:
        return "No"
    if ext not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
```

This Python script divides the given file name into its locus (letters) and extension (after the dot), and checks the conditions of validity for both of them. So, it returns 'Yes' if the name is valid, and 'No' otherwise. This aligns with the problem statement, so the script is correct. 

Here's the separated explanation for the markdown code block:
```python
def file_name_check(file_name):
    locus, ext = file_name.split('.')
```

- The function `file_name_check` takes a single argument, `file_name`, which is a string representing the name of a file.
- The script splits this file name at the dot ('.') character. This results in two strings: `locus` and `ext`.
- `locus` contains everything from the start of the file name up to, but not including, the dot.
- `ext` contains everything from the dot to the end of the file name.
- Therefore, this code block neatly separates the file name for more convenient checks. 

```python
    if len(locus) == 0 or not locus[0].isalpha():
        return "No"
```

- The script first checks if the length of `locus` is zero. If it is, it returns "No" immediately, as an empty locus means the file name is invalid.
- If the locus is not empty, it proceeds to check if the first character of the locus is a letter using the `isalpha()` method. If not, it also returns "No" since the file name is invalid.
- Once again, if the condition is true, it means the file name is valid so far, so the script continues with the next checks. 

```python
    if len(locus) > 3:
        return "No"
```

- Here, the script checks if the length of `locus` is greater than 3. If it is, it returns "No" since this means the file name is invalid.
- If the locus length is within the limit, the script continues to check the extension. 

```python
    if ext not in ['txt', 'exe', 'dll']:
        return "No"
```

- The script checks if the extension, `ext`, is not among the permitted extensions: ['txt', 'exe', 'dll']. 
- If the extension is not one of these, the file name is invalid, so the script returns "No". 

```python
    return "Yes"
```

- If all the previous checks have passed, the file name is valid, and the script returns "Yes". 

This code block allows for efficient and organized checking of different file name conditions. It first validates the locus and then the extension, which aligns with the problem statement. In the given markdown code block, the function `file_name_check` takes a file name as input and returns "Yes" if the name is valid and "No" otherwise. The function first splits the file name into its locus (before the dot) and extension (after the dot). It then checks the following conditions:
1. The locus should not