```python
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separates a string of balanced parentheses into individual groups.

    : Return list of separated strings.

    parent: []
    return []
    ```

    def get_balanced_pair(pair: str) -> str:
        """
        Checks if a pair of parentheses is balanced

        Returns: The correctly balanced version of the pair.
        """
        return '(' + pair[0] + pair[1] + ')'

    return [get_balanced_pair(pair) for pair in zip(parentheses.split(), '()')]
```
This code defines a function, `separate_paren_groups`, that takes a string of parentheses as input and returns a list of separated strings. 

The code also defines a helper function, `get_balanced_pair`, which checks if a pair of parentheses is balanced and returns the correctly balanced version of the pair. 

Finally, the `separate_paren_groups` function uses the helper function to split the input string of parentheses into individual groups, each group being a balanced pair of parentheses.