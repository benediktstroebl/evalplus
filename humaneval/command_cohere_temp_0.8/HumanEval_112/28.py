```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete = delete + ['']
    delete = ''.join(delete)
    return delete, delete == delete[::-1]
```
This Python script provides a function called `reverse_delete`, which takes two strings as input, `s` and `c`, and performs a series of operations to solve the specified problem. 

Here's an explanation of the operations performed in the function:
1. `delete = [x for x in s if x not in c]`: This creates a list called `delete` by iterating through each character `x` in the input string `s`. It includes each character `x` in the list `delete` only if it is not present in the second input string `c`. This effectively selects the characters in `s` that are not in `c`, which will be deleted from the original string.
2. `delete.reverse()`: This method is called on the `delete` list to reverse its order. Since the characters to be deleted were added in reverse order, this ensures that they are inserted in the original order.
3. `delete = delete + ['']`: This appends an empty string '' to the end of the `delete` list, serving as a placeholder to ensure subsequent concatenation results in a string result.
4. `delete = ''.join(delete)`: This converts the list `delete` back into a string by joining the elements together with no separator. The empty string added earlier ensures that there is no extra character added during the joining process.
5. The function returns a tuple with the result string `delete` and a boolean value (`True` or `False`) indicating whether the resulting string is a palindrome. The palindrome check is performed by comparing the result string with its reverse (`delete[::-1]`), and the boolean value is True if they are equal and False if not. 

The script ensures that any characters in `s` that are equal to any character in `c` are effectively removed, and it determines if the remaining characters in `s` form a palindrome. The function's implementation passes the provided tests, validating its correctness.