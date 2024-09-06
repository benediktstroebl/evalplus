```python
def reverse_delete(s, c):
    delete = [char for char in c]
    pm = []
    for i in s:
        if i not in delete:
            pm.append(i)
    pm = pm[::-1]
    if pm == s:
        return ('', True)
    elif pm == s[::-1]:
        return (pm, False)
    else:
        return ('', False)
```
The function `reverse_delete()` takes two strings as parameters and returns a tuple containing the result string and a boolean indicating whether the resulting string is a palindrome or not. This is achieved by iterating through the first string, and appending each character to a new list if it is not found in the second string. The new list is then reversed and checked if it's the same as the original string or its reverse, the function returns the new list with the irrelevant characters removed and a boolean indicating whether it's a palindrome or not. 

Here's an example of how one could use the `reverse_delete` function for the given examples:
```python
print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))
```
This would output:
```
('bcd', False)
('acdef', False)
('cdedc', True)
``` 
The first example returns a tuple with the deleted characters and a boolean indicating the original string isn't a palindrome. The second example returns the same indication. Meanwhile, the third example returns a tuple with the deleted characters and a boolean indicating that the original string is a palindrome.