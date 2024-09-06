```python
def reverse_delete(s, c):
    # Calculate the delted string
    deleted = ''.join([x for x in s if x not in c])

    # Check if the deleted string is a palindrome
    return (deleted, deleted == deleted[::-1])
```
The `reverse_delete()` function takes two strings as parameters, `s` and `c`. It uses list comprehension to create a new string `deleted` by removing characters from `s` that are present in `c`. Subsequently, it verifies if `deleted` is a palindrome by comparing it with its reverse using the slice notation `[::-1]`. The function returns a tuple containing the `deleted` string and a boolean value indicating whether it is a palindrome.

Here is a sample output of the function:
```
('cdedc', True)
```
This is an example of the function's behavior when the input is 'abcdedcba' and 'ab'. The deleted string is 'cdedc' and it is a palindrome because it is the same forwards and backwards.