```python
def match_parens(lst):
    open_tup = tuple(char for char in lst[0] if char == '(')
    close_tup = tuple(char for char in lst[1] if char == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

This approach involves destroying the input strings as they are not required to be returned for this problem, and we can directly verify if the lengths of (' and ) are equal or not. We do this by using tuple conversion, where all occurrences of a character in a string are converted into a tuple, which orders the characters in alphabetical order. We can then compare the lengths of the two tuples to check if the parentheses can be matched. This returns "Yes" if the length of open and close parentheses is equal and returns "No" otherwise. 

Here is an example of how to use this function:
```python
print(match_parens(["(", ")"])) # Output: Yes
print(match_parens(["(", "("])) # Output: No
``` 
This would output:
- Yes
- No
respectively, indicating the availability of matching parentheses in the first example but not in the second.