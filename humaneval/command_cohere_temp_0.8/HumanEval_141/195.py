```python
def file_name_check(file_name):
    fo = []
    d = dict()
    n = file_name.split('.')
    if len(n) == 2:
        if n[0].isalpha() and n[0].strip() != '':
            s = n[0]
        else:
            return 'No'
        if len(n[1]) == 3 and n[1].isdigit():
            t = n[1]
        else:
            return 'No'
        if t in d:
            fo.append(d[t])
        else:
            d[t] = len(fo)
            fo.append(t)
        if len(fo) <= 3 and s + '.' + t == file_name:
            return 'Yes'
    return 'No'
```

The code divides the analysis of the string into several parts, improving readability and simplifying the logic of the checks, making the code more robust and easier to maintain, as well as passing the given tests. 

The first conditional statement checks if the passed file name is divided into two parts by the dot ('.'). This is done by using the `split('.')` method on the file name, which returns a list with the first element being the substring before the dot and the second element having the substring after the dot. If there are not two elements in the list, then the file name does not qualify under the given conditions, and thus the function returns 'No'. 

The next part of the code initializes an empty list `fo` and an empty dictionary `d`, which are used to store the three-digit strings and hold them in the list or add them to the dictionary for later use. It also stores the first part of the divided string into a variable `s` and the second into a variable `t`. The if statement then checks if the second part, `t`, contains three characters and if these characters are digits. This is done by utilizing the `isdigit()` method in Python, which checks if the passed string consists of digits only. If this is not the case, then the function returns 'No'. 

If the previously mentioned checks are passed, the code then checks if the string after the dot is a key in the dictionary `d`. If it is, it means that this string has already been counted, and the corresponding value of the count is retrieved from the dictionary. If it is not, then the current number of occurrences of this string is assigned to the value of one, and the string is added to the list `fo`. This is done in order to optimize the code and avoid repetitive string comparisons. 

The last conditional statement checks if the length of the list `fo` is less than or equal to three, and if the string concatenated by the dot qualifies as the file name. If so, this would mean that there are not more than three files with a name that contains three digits, and the function returns 'Yes'. 

The code ensures the execution of the task with a simplified and optimized version of the original problem statement, thus being more concise and easier to understand.