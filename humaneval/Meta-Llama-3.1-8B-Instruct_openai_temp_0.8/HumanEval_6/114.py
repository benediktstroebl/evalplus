```python
from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    :param paren_string: Input string containing groups of parentheses.
    :return: List of deepest levels of nesting for each group.
    """
    # Split the input string into groups based on spaces
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Use regular expression to find all substrings that are balanced (i.e., have matching parentheses)
        balanced = re.findall(r'\([^()]*\)', group)
        
        # Initialize the maximum level of nesting
        max_level = 0
        
        # Iterate over each balanced substring
        for substring in balanced:
            # Calculate the level of nesting for the substring
            level = substring.count('(') - substring.count(')')
            
            # Update the maximum level of nesting
            max_level = max(max_level, level)
        
        # Append the maximum level of nesting for the current group to the results
        results.append(max_level)
    
    # Return the list of results
    return results


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a regular expression to find all substrings in each group that are balanced (i.e., have matching parentheses). It then calculates the level of nesting for each balanced substring by counting the number of unmatched open and close parentheses. The maximum level of nesting for each group is stored in the results list.