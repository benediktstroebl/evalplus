```python
def parse_nested_parens(s: str) -> List[int]:  # function to parse nested parentheses
    def get_max_depth(s: str) -> int:  # helper function to get the deepest level of nesting
        return len(s) - sum(1 for i in range(1, len(s)) if s[i] == '(')
    
    p = ["("] * get_max_depth(s) + ")" * get_max_depth(s[::-1])
    return [i for i, x in enumerate(p) if x == ")"]
```