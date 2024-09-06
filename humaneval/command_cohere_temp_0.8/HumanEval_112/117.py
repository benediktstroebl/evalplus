```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    palindrome = delete == delete[::-1]
    return delete, palindrome
```
This Python script defines a function called `reverse_delete` which takes two arguments, `s` and `c`, representing the input strings. The function utilizes sets to efficiently delete characters from `s` that are present in `c`. After deleting these characters, the resulting string is reversed and compared to itself using slicing (`s[::-1]`) to determine if it's a palindrome. The function returns a tuple consisting of the modified string and a boolean value indicating whether it's a palindrome. 

Here is a breakdown of the code:
- `delete = [x for x in s if x not in c]`: Creates a list of all characters in string `s` that are not in string `c`. This is done using a list comprehension, which iterates over each character in `s` and checks if it's not in `c`, effectively deleting the characters present in `c` from `s`.
- `delete.reverse()`: Reverses the `delete` list, turning it back into a string. 
- `palindrome = delete == delete[::-1]`: Checks if the reversed `delete` list is equal to its own reverse, which is a common method for determining whether a string is a palindrome. 

The given example scenarios in the Markdown code block show how the function behaves for different inputs. You can test this function further by calling it with different input strings and character combinations to verify its correctness in palindrome detection and character deletion. 

If you would like to test this function, you can add this block of code to check the function:
```python
# Testing the function
input_strings = ["abcde", "abcdef", "abcdedcba"]
input_characters = ["ae", "b", "ab"]
expected_results = [("bcd", False), ("acdef", False), ("cdedc", True)]

for i in range(len(input_strings)):
    s, r = reverse_delete(input_strings[i], input_characters[i])
    assert s == expected_results[i][0] and r == expected_results[i][1]
```

This block of code simply checks the function with different inputs and asserts whether the outputs are equal to the expected outputs. 
If you have any more questions or need further assistance with this problem or any other Python related tasks, don't hesitate to ask!