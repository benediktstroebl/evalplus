```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```

This approach utilizes the `re.findall` method in combination with the regular expression pattern `\w+` to extract all the words from the given string. The pattern `\w+` matches one or more alphanumeric characters, allowing for words comprising of letters, numbers, and underscores. 

To retain the clarity of the original prompt, I'll provide the above code within a Markdown code block, as requested:
```
```python
import re

def words_string(s):
    return re.findall(r'\w+', s)
```
```

You can insert the input strings `"Hi, my name is John"` and `"One, two, three, four, five, six"` into the script and check the function's corresponding output, which should be:
```
['Hi', 'my', 'name', 'is', 'John']
['One', 'two', 'three', 'four', 'five', 'six']
``` 
This reinforces the efficacy of the function in splitting the provided strings into individual words.