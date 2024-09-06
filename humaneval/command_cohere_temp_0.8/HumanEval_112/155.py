```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` taking two strings as parameters (`s` and `c`). It deletes characters from `s` that are present in `c`, and then checks if the remaining string is a palindrome. The function returns a tuple containing the updated string after deleting characters and a boolean value indicating whether the remaining string is a palindrome (True if it is a palindrome and False if it isn't). 

To correctly solve this problem, the script uses a list comprehension to create a new string containing the characters present in the original string `s` but not in the string `c`. The script then reverses this new string and appends it to the original string. This effectively deletes the characters present in `c` from `s`. The script then checks if the modified string is a palindrome by comparing it to its reverse using the `reverse` and `==` techniques. The function returns a tuple containing the modified string and a boolean indicating whether it's a palindrome (True if it is, and False if it isn't). 
You can test this function by calling it with different input strings `s` and a character string `c` to see the resulting deleted string and whether or not the remaining string is a palindrome.