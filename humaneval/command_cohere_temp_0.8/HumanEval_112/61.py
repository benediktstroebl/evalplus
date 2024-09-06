```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    result = ''.join(char for char in s if char not in delete and char in reverse)
    return result, result == result[::-1]
```

The problem asks to create a function `reverse_delete(s,c)` that takes two strings as input, `s` is the main string that will be manipulated, and `c` is the string against which the characters in `s` will be compared and possibly deleted if found. 

The function returns a tuple containing the manipulated string `s` after removing characters that are present in `c`, and a boolean indicating whether the resulting string is a palindrome. This is achieved by:
1. Creating a list `delete` that contains all the characters present in `c`. This allows for easy deletion of these characters from `s` by iterating over `delete` and removing characters in `s` that are also in `delete`.
2. Unlike the above deletion, we want to keep the character if it appears in the reverse complement (`reverse`) but not in `delete`, this ensures that characters that are not deleted but are present at the start and end of the string, will make the string a palindrome only if they are symmetrically positioned. This leads to the line:
    ```python
    result = ''.join(char for char in s if char not in delete and char in reverse)
    ```
3. The final string is then returned along with a boolean indicating whether it is a palindrome, which is evaluated as:
    ```python
    return result, result == result[::-1]
    ```

The provided code uses list comprehensions and joins strings using a generator expression, which are both efficient and readable ways to perform the described operations. The code also effectively manipulates strings and tests for palindromes, making it a suitable solution for the problem. 

This problem can be solved using a variety of approaches and styles, so the solution is not unique. The above is one self-contained Python script that solves the problem in a markdown code block.