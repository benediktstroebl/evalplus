Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of separate groups of parentheses. The code is formatted with a markdown code block and inline comments to explain each section:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    """
    # Define a helper function to check if a given char is an open or close paren
    def is_open_paren(c: str) -> bool:
        """ Returns true if the given char is an open paren (weiler compatibility) 
        This is a helper function and doesn't include actual opening/closing logic """
        return c == '(' or c == '[' or c == ' {'
    # Define a helper function to check if a given string has a closing parenthesis 
    def has_closing_paren(s: str) -> bool:
        """ Returns true if the given string has a closing parenthesis that matches some opening parenthesis in the string 
        (ignore spaces) """
        return s[-1] == ')' or s[-1] == ']' or s[-1] == '}'
    # Define a helper function to get the balance of a given string
    def paren_balance(s: str) -> int:
        """ Returns the balance of a given string, with the following rules:
        * An open paren adds 1 to the balance
        * A closing paren subtracts 1 from the balance
        * If the string is empty, the result is 0
        """
        balance = 0
        for c in s:
            if is_open_paren(c):
                balance += 1
            elif has_closing_paren(s):
                balance -= 1
        return balance
    
    # Define a main function to actually solve the problem:
    def separate_groups(string_list: List[str]) -> List[str]:
        """ Returns a list of strings, each string containing a separate group of parentheses 
        (ignore spaces) """
        separated_groups = []
        open_list = []
        for s in string_list:
            # If the string is not empty and has a balance of 0, add it to the list of groups
            if not s == "" and paren_balance(s) == 0:
                separated_groups.append(s)
            # If the string is an open paren, add to the list of opens to find the matching close
            elif is_open_paren(s[-1]):
                open_list.append(s)
            # If the string is a close paren and it matches something in the open list, pop that item and decrement the balance
            elif has_closing_paren(s):
                try:
                    open_idx = open_list.index(s[0:len(s)-1])
                    open_list.pop(open_idx)
                except:
                    pass
            # Close the shortest open group possible (to avoid nested groups)
            while open_list and paren_balance(open_list[0]) == 0:
                separated_groups.append(open_list.pop(0))
        return separated_groups
    paren_string = "(" + "  " * 25 + "(((" + "  " * 24 + ")))" + "  " * 23 + ")"
    # Test the