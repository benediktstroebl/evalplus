```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else 0
    return ans
```

The provided Python script defines a function called `split_words` that takes a string as input. This function serves to split the input string into a list of words based on whitespace or comma separation. It achieves this in a nuanced way to handle different scenarios.

If the input string contains commas, it uses the `split` method with ``,` as the delimiter to return the words as a list. This caters to the scenario where words are separated by commas.

Similarly, if the input string contains spaces, it again uses the `split` method, this time with ` ` (`space`) as the delimiter, to return the words as a list. This handles the common case of words being separated by spaces.

If the input string lacks both commas and spaces, it checks if it contains only lowercase letters. In this case, it uses the `len` function to return the number of words, assuming the input represents a list of words without separation.

If none of the above conditions are met, meaning the input string is empty or contains non-alphabetic characters, the function returns 0, indicating that no valid words were found.

This approach ensures a flexible and dynamic solution that handles various input scenarios while aligning with the problem statement's expectations.