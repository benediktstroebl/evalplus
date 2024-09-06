```python
def split_words(txt):
    words = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return words if words is not None else [txt]
```

This script employs a conditional structure to determine the appropriate base function to call for splitting the string into words. The base functions are `split()` for splitting on spaces and `split()` for splitting on commas. In the case where the input string lacks whitespace and comma characters, the function returns the string's length when reduced to alphanumeric characters using the `isalpha()` function. This occurs unless the string is empty, in which case the function returns `None`. Finally, the function applies a conditional check to ensure that the returned list of words is not `None`, replacing it with the raw input string as the default case.

The `split_words` function is subsequently tested for compliance with problem descriptions using the following inputs:
```python
test_split_words("Hello world!", ["Hello", "world!"])
test_split_words("Hello, world!", ["Hello", "world!"])
test_split_words("abcdef", ["a", "b", "c", "d", "e", "f"])
test_split_words("amazon.com", ["amazon", "com"])
test_split_words(",,,,,,,", [",", " ", ",", ",", ",", ",", ".", "!"])
test_split_words("queenbeeayehyeah", ["queenbee", "ayehyeah"])
```

Each test is run against the `split_words` function, and the result is compared to the expected output. 
The `split_words` function is designed to provide a list of words split from the input string based on whitespace or comma delimiters, returning the input string itself as a last resort. 

To ensure the function works as intended, it's crucial to consider corner cases such as input with inconsistent whitespace, comma, and alphanumeric only inputs. 
The provided tests cover a broad range of scenarios and are not exhaustive, allowing for more test scenarios to further validate the function's correctness. 
It's always good practice to add more tests to cover more scenarios and edge cases to ensure that the function is flexible enough to handle various input types.