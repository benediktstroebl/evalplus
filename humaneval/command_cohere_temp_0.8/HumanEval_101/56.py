```python
import re

def words_string(s):
    return re.findall(r'\b\w+\b', s)
```

This approach utilizes the `re.findall` method in conjunction with the regular expression pattern `\b\w+\b` to accurately capture individual words from the given string, regardless of whether commas or spaces separate them. This ensures that the function can handle a wide range of input scenarios while correctly returning an array of words.

Here is a more detailed explanation of the code:
- The import statement `import re` brings in the Python `re` module, which offers powerful capabilities for working with regular expressions.
- The `def words_string(s):` line defines a function named `words_string` that takes a single argument `s`, which is the input string containing a list of words separated by commas or spaces.
- Within the function, the line `return re.findall(r'\b\w+\b', s)` leverages the `re.findall` function to search the input string `s` for all occurrences of the regular expression pattern `\b\w+\b`.
- The regular expression pattern `\b\w+\b` is constructed as follows:
  - `\b`: Ensures the capture of a whole word by matching a word boundary, which is a position that cannot be a suffix or prefix of another word.
  - `\w+`: Matches one or more word characters, which include alphabets (both uppercase and lowercase), digits, and underscores.
- As a result, `re.findall` collects all the matched words from the input string and returns them as a list.

This function efficiently splits the input string into words, regardless of the separation characters, and provides an array of the words as its output.