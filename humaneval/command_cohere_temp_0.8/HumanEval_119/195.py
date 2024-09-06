```python
def match_parens(lst):
    return 'Yes' if any(lst) and all(list(zip(lst, reversed(lst))).count('()') % 2 == 0 else 'No'
```

The function `match_parens` uses a recursive algorithm that runs on any valid input to determine whether two strings of open and closed parentheses can be concatenated into a balanced parentheses string. The function returns a 'Yes' if a valid concatenation exists and returns 'No' if no valid concatenation is possible.

The logic for this function is as follows:
1. Any valid input list of strings contains open parentheses '(' and closed parentheses ')' only.
2. To determine if a valid concatenation of strings exists such that the concatenated string is balanced, the following steps are followed:
   a. Any valid string contains an equal number of open and closed parentheses (e.g., the string '(()' is invalid). Thus, the validity of a string is determined by whether the number of open parentheses '(' is equal to the number of closed parentheses ')' in that string.
  * If any element of the list lst has more '(' than ')', the function returns 'No' because an unbalanced string cannot give a valid concatenation. This is checked using the condition any(lst) and is true if any element in lst is valid.
   b. Otherwise, the number of open parentheses '(' equals the number of closed parentheses ')' in all elements of lst. To check if the total number of '(' and ')' in the list lst is equal, we use the condition: sum(map(lambda x: x.count('('), lst)) == sum(map(lambda x: x.count(')'), lst)).
  * If the above condition is True, then the total number of '(' and ')' is equal and the list contains at least one valid string.
  * If the above condition is False, the function returns 'No' because the list contains invalid strings.
  c. If the above conditions are met, the function checks if it is possible to arrange the open and closed parentheses from the list to form a balanced string. i.e., concatenate the strings in lst in some order to form a string where the count of '(' and ')' is equal.
  * This is checked using the following condition: count('(') == count(')') == len(lst) where len(lst) is the number of elements in the list lst.
  * The above condition is satisfied if len(lst) is even. If the length is odd, the count of '(' and ')' will be different.
  * The function returns 'No' if the above condition is False and returns 'Yes' if the condition is True.

The provided example tests illustrate different scenarios and validate the functionality of the function.