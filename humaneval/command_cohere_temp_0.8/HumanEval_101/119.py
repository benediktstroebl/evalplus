```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes regular expressions, specifically the word matching (`\w+`) regular expression, to efficiently split the string into words regardless of whether the separators are commas or spaces. This solution is more concise and effective than using string split(), as it handles multiple types of separators in a single step.

Here is an example usage of the code:
```python
print(words_string("Hi, my name is John"))
```

The output of the example usage will be:
```
['Hi', 'my', 'name', 'is', 'John']
```

This demonstrates how the `words_string` function correctly splits the input string "Hi, my name is John" into an array of words.