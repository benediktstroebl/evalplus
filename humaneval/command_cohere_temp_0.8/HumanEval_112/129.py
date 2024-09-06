```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == s else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two arguments, `s` and `c`. This function essentially processes the string `s` to remove characters that are present in the string `c`, and then it checks if the modified string is a palindrome. The steps are as follows:

1. Create a list `delete` that contains all the characters from string `s` that are not present in string `c`. This is done using Python's list comprehension, which filters out characters that are in `s` but not in `c` resulting in a new list.    
2. The characters that were not deleted from `s` are then reversed using the `reverse()` method, which is necessary to eventually determine if the modified string is a palindrome.  
3. The palindrome check is then conducted by comparing the reversed `delete` list to the original `s` string. If the two are equal, the result is True, otherwise, it is False. 

Finally, the function returns a tuple consisting of the `delete` list and the `palindrome` boolean value. 

This solution is efficient with time complexity of O(n log n) where n is the length of s and linear space complexity of O(n). 

A simpler solution could be a two-step process where:

1. Delete all characters in s that are present in c
2. Check if the resulting string is a palindrome 

An optimal time solution would be to match the deletion process with the checking process, this can be done using a hashmap approach, where we look at the char in s, if it's in the hashmap as present, we skip it, if it's not we add it to the result string and reverse it to check for the palindrome while constructing it.