```python
import re

def split_words(txt):
    ans = re.findall(r'\w+|[.,]', txt)
    if len(ans) == 1 and ans[0].isalpha():
        return len(ans[0])
    return ans
```

The function leverages regular expressions to efficiently split the input text into words or numbers, depending on the content.

The pattern `[.,]` captures comma groups and dot separators, while `\w+` captures word sequences. The `re.findall()` function retrieves all occurrences of the pattern.

If only one capturing group is found and it consists of alphabetic characters, the function determines the number of characters, considering both uppercase and lowercase. This case is treated separately because it doesn't involve any splitting and serves as a fallback when no separators are present. 

The resulting list of captured groups or character count is then returned, based on the content and structure of the input text.  This approach ensures the function's versatility in handling various input scenarios.