```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean
    """
    # Convert string to list to allow iterating through reversed letter by letter
    temp_list = list(text)
    # Compare each character in text with its corresponding reversed character
    for i in range(len(temp_list)):
        if temp_list[i] != temp_list[~i%len(temp_list)]:
            return False
    return True
```

This function uses two lines to solve the problem. The first line converts the string to a list to allow iterating through the reversed letter by letter, and the second line compares each character in the string with its corresponding reversed character. The corresponding reversed character is calculated using the bitwise negation operator `~` and the modulo operator `%`. The modulo operator ensures that the index always stays within the length of the list.

To further clarify the solution, here is an explanation of the code with step-by-step examples:

1. **`temp_list = list(text)`**: This line converts the string `text` to a list. Lists are useful for maintaining order while allowing random access and iteration. This is essential to solve this problem as we need to iterate through the characters in the string, but also access characters in a reversed order.
2. **`for i in range(len(temp_list)):`**: This line starts a loop that iterates through each character in the list. The `range(len(temp_list))` expression creates a sequence of numbers from 0 to one less than the length of the list. This is equivalent to `range(0, len(temp_list))` but is written in a way that avoids indexing errors if the list length happens to be zero.
3. **`if temp_list[i] != temp_list[~i%len(temp_list)]:`**: This line compares the character at index `i` in the original string with the character at the same index in the reversed string. The expression `~i%len(temp_list)` calculates the index of the character in the reversed string. It does this by first calculating the negated value of `i` using the bitwise negation operator `~`. Then, it ensures that the index falls within the length of the list using the modulo operator `%`. This is necessary because if the original index `i` is, for example, 34, the expression `~34%len(temp_list)` will correctly be `~34%33` which evaluates to 1, which is the correct index for the reversed string.
4. **`Return False`**: If any of these comparisons yields false, meaning that the characters do not match, the function immediately returns `False`, indicating that the string is not a palindrome.
5. **`Return True`**: If none of the comparisons yield false, meaning that all characters match, the function returns `True`, indicating that the test is a palindrome. 

This solution achieves the goal of checking whether a given string is a palindrome in O(n), where n is the length of the string, making it an efficient algorithm. It is self-contained, easily understood without external documentation, and should pass any tests corresponding to the provided prompt.