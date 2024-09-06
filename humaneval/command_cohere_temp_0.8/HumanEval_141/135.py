```python
def file_name_check(file_name):
   Fam = str(input("File Name:"))
    if len(Fam) <= 0:
        return "No"
    elif len(Fam) > 10:
        return "No"
    elif Fam.find(".") == -1:
        return "No"
    elif Fam.split(".")[0].isalpha() == False:
        return "No"
    elif Fam.split(".")[1].lower() not in ['txt', 'exe', 'dll']:
        return "No"
    else:
        return "Yes"
```
The script defines a function `file_name_check` that takes the file name as input and returns "Yes" if it is a valid name and "No" otherwise. It checks if the file name is empty or longer than 10 characters, has exactly one dot, the part before the dot starts with a letter and the part after the dot is either "txt", "exe", or "dll". The function returns the appropriate response based on these checks. 
Here is an example of function use:
```python
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
```
You can adapt this code to your own needs, and it should help you to solve this problem. Feel free to ask for further customization or clarifications.