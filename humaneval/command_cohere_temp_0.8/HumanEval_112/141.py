```python
def reverse_delete(s, c):
    delete = [char for char in c]
    result = ''.join([char for char in s if char not in delete])
    return result, result == result[::-1]
```
The function `reverse_delete()` takes two strings, `s` and `c` as input and returns a tuple containing the result of deleting characters from `s` that are present in `c`, and a boolean indicating whether the resultant string is a palindrome. The `delete` list is used to store characters from `c` for easy deletion in the `s` string. After deleting these characters from `s`, it is checked whether the resultant string is a palindrome or not, and the function returns a tuple with these two values. 

Here is an example usage of the function:
```python
print(reverse_delete("abcde", "ae")) 
print(reverse_delete("abcdef", "b")) 
print(reverse_delete("abcdedcba", "ab"))
```
This would produce the following output:
```
('bcd', False)
('acdef', False)
('cdedc', True)
``` 
The function passes the tests corresponding to the specified problem. It handles various cases, including different lengths of `s` and `c`, and different sets of characters in `s` and `c`.