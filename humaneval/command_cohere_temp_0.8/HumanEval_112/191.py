```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

The Python script provided defines a function `reverse_delete` taking two strings as input, `s` and `c`, performing the task as described in the problem statement. 

The function first creates a list `delete` containing all characters from string `s` that are not present in string `c`. To achieve this, it uses the list comprehension `[x for x in s if x not in c]`, which creates a list of all elements in `s` that are not in `c`.

Following that, the function reverses the `delete` list using the `reverse()` method, then appends to `delete` all characters from `s` that _are_ in `c`. This step ensures that any characters in `s` that are also in `c` are placed at the end of the `delete` list, effectively deleting them. 

The function returns a tuple containing the `delete` list and a boolean value indicating whether the resulting string is a palindrome. To check if the `delete` list forms a palindrome, the function uses the slice notation `delete[::-1]` to reverse the list and compare it with the original `delete` list. 

Overall, this code provides an efficient and concise solution to the problem, and should prove useful for anyone seeking a palindrome verification mechanism for strings with deleted characters.