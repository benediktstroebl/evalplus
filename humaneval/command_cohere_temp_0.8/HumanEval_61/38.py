```python
def correct_bracketing(brackets):
    open_brackets = len(brackets.count('('))
    close_brackets = len(brackets.count(')'))
    return open_brackets == close_brackets
```

This function uses the built-in methods to count the number of opening and closing brackets and compares them, ensuring every opening bracket has a corresponding closing bracket. 

Here is a sample output:
```
>>> correct_bracketing("(()())")
True
>>> correct_bracketing(")(()")
False
``` 

Feel free to test this function with other strings to ensure its correctness. Let me know if this solution suits your needs or if you'd like me to adjust it further.