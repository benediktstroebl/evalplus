```python
def fix_spaces(text):
    new_text = []
    for c in text:
        if c == ' ':
            if len(new_text) > 1 and new_text[-1] == ' ' and new_text[-2] == ' ':
                new_text.append('-')
            else:
                new_text.append('_')
        else:
            new_text.append(c)
    return ''.join(new_text)
``` 

The code uses a for loop to iterate over each character in the `text` string. When it encounters a space, it checks the previous two characters. If they are both spaces, it appends a `-` to the `new_text` list instead of an underscore. Otherwise, it appends an underscore. This is done using the conditional `if len(new_text) > 1 && new_text[-1] == ' ' && new_text[-2] == ' '`. The output is then returned as a string using ''.join(new_text), which conjoins all the elements in the list with nothing in between. 

The following tests would verify the correctness of the function: 
```python
fix_spaces("Example") == "Example"
fix_spaces("Example 1") == "Example_1"
fix_spaces(" Example 2") == "_Example_2"
fix_spaces(" Example   3") == "_Example-3"
```
This problem can also be solved using Python's regex, providing a more concise solution. Below is an example of how this approach can be implemented: 
```python
import re

def fix_spaces(text):
    return re.sub(r'\s+', r'_\s*|\s*-\s*', text)
```

In the above code, `re.sub` is a function that replaces the matches of a pattern with a specified string. The pattern `r'\s+'` matches one or more whitespace characters (the `\s` matches a whitespace character and `+` specifies the repetition). The `r'_\s*|\s*-\s*'` replacement specifies that consecutive spaces should be replaced with either underscores or hyphens. The underscore (`_`) is used if there are no other characters (e.g. two consecutive spaces). The result of the replacement is then returned.