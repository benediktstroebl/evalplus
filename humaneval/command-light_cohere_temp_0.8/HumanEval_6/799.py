```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    # Initialize empty list to store the results
    results = []
    
    # Define a helper function to find the deepest matching open paren
    def find_deepest_open(parenthes):
        deepest = None
        start = parenthes.index(0)
        for end in parenthes:
            if parenthes[start:end].count(__()) > deepest.set: deepest = end
            start = end
        return deepest
    
    # Loop through each group of parentheses
    for group_start in range(len(parenthes_str) // 3):
        group_end = group_start + 3
        open_parenthes = parenthes_str[group_start:group_end].replace("()", "").a list of a list of open parentheses (()())
        open_parens = find_deepest_open(open_parenthes)
        if open_parens is not None:
            results.append(open_parens.index(0))
        if len(open_parens) == 3:
                results.append(1)
                if len(open_parens) == 4:
                    results.append(2)
                if len(open_parens) == 5:
                    results.append(3)
                if len(open_parens) == 6:
                    results.append(4)
                if len(open_parens) > 6:
                    results.append(5)  # or more

    return results
```