```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`. This function uses two arrays, `delete`, and `palindrome`. The `delete` array is populated with characters from string `s` that are not included in string `c`, this is achieved using a list comprehension where a character is added if it is not in the other string (`c`). Then, the `delete` array is reversed using the `reverse` method to achieve the "deletion" task, and the `palindrome` array is compared to its reverse using the `==` operator. If the two arrays are equal, then the `palindrome` variable is set to `True`, otherwise, it is set to `False`. This function returns a tuple of (`delete`, `palindrome`) where `delete` is the string that `s` was transformed into and `palindrome` is a boolean indicating whether the transformed string is a palindrome or not. 

Here is an example usage of this function:
```python
s = "abcdedcba"
c = "ab"
r, p = reverse_delete(s, c)
print(r) #cdedc
print(p) #True
```
In this example, the `delete` array would be `['c', 'd', 'e', 'd', 'c', 'b', 'a']` and the `palindrome` array would be `['c', 'd', 'e', 'd', 'c', 'b', 'a']`, because these are the characters in `s` that are not in `c` and the reversed array is the same as the original, so the output would be `cdedc` and `True`. 

This is just one example of how to solve the problem, and there are many other ways to write a Python script that achieves the same result. 
If you want to improve this script, you can add some input and error-handling statements to the code, such as the ones below:
```python
def reverse_delete(s, c):
    if not isinstance(s, str) or not isinstance(c, str):
        raise ValueError("Input must be strings!")
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return delete, palindrome

# Example usage:
s = "abcdedcba"
c = "ab"
try:
    r, p = reverse_delete(s, c)
    print(r) #cdedc
    print(p) #True
except ValueError as e:
    print(e)  #Input must be strings!
``` 

This additional code helps to ensure that the input is valid and can help prevent errors when running the script.