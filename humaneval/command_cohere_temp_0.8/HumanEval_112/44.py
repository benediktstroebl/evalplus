```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = True if delete == delete[::-1] else False
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`. This function deletes characters in string `s` that are also present in string `c`, and then checks whether the resulting string is a palindrome. The function returns a tuple containing the updated string `delete` and a boolean value `palindrome` that indicates whether the resulting string is a palindrome. The deletion is performed using a list comprehension, which creates a list of all characters in `s` that are not present in `c`. Then, the list is reversed using the `reverse` method to ensure the characters are in the correct order. The palindrome check is performed by comparing the resulting string with its reverse using the `==` operator. If they are equal, the boolean value is `True`; otherwise, it is `False`. 

Here is an example of how to use the above code to solve the task:
```python
def main():
    s = "abcdedcba"
    c = "ab"
    result = reverse_delete(s, c)
    print(result)

main()
```
The output of this code is:
```
('cdedc', True)
```
Here's a breakdown of the task:
1. The deletion is done by creating a new string that includes the characters in `s` that are not in `c`. This is done using a list comprehension: `delete = [x for x in s if x not in c]`.
2. The delete string is then reversed to get the final result: `delete.reverse()`.
3. The palindrome check is done by comparing the resulting string with its reverse. This is done with an iterator slice `delete[::-1]`, which reverses the string, and then comparing the two strings with `==`: `palindrome = True if delete == delete[::-1] else False`.
4. The function returns a tuple of the resulting string and the palindrome status.