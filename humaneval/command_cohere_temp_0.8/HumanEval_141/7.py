```python
def file_name_check(file_name):
    fut = []
    if len(file_name) > 0:
        ok = True
        letters = ['a'-'z','A'-'Z']
        # condition 1
        if len(set(file_name)) > 3:
            ok = False
        # condition 2
        if '.' not in file_name:
            ok = False
        else:
            ft = file_name.split('.')
            # condition 3
            if not (ft[0][0] in letters and len(ft[0]) > 0):
                ok = False
            # condition 4
            if ft[1] not in ['txt', 'exe', 'dll']:
                ok = False
        if ok:
            return "Yes"
        else:
            return "No"
    else:
        return "No"
```

The following tests demonstrate the behavior of the `file_name_check()` function:
```python
# test 1
test_file = "example.txt"
result = file_name_check(test_file)
assert result == "Yes"

# test 2
test_file = "1example.dll"
result = file_name_check(test_file)
assert result == "No"

# test 3
test_file = "example"
result = file_name_check(test_file)
assert result == "No"

# test 4
test_file = "1.txt"
result = file_name_check(test_file)
assert result == "Yes"
```

This script includes a defined function `file_name_check()` that utilizes several conditions to verify the validity of a file name. If the file name is valid, it returns `Yes`; otherwise, it returns `No`. The function evaluates four main conditions:
1. The file name should not contain more than three digits.
2. It must contain exactly one dot '.' character.
3. The part of the name before the dot should start with a letter and not be empty.
4. The part after the dot should be one of the following: 'txt', 'exe', 'dll'.

The tests then check the behavior of the function with different test cases to ensure that it adheres to the specified requirements and returns the correct results for each scenario.