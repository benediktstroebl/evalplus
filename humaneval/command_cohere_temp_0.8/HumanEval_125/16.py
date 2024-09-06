```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(txt) if txt.isalpha() else None
    return ans
```

The problem requires splitting a string of words into a list of words while handling various edge cases. The method splits the input text based on whitespace or commas. If neither whitespace nor commas are found, the function checks if the text contains only lowercase letters, in which case it returns the total count of letters. If the input is not a string or contains non-alphabetic characters, an None is returned.

Here is a test suite to check if the function behaves as expected:
```python
def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello, world!") == ["Hello", "world!"], "split on commas"
    assert split_words("abcdef") == 3
    assert split_words("abc") == ["a", "b", "c"]
    assert split_words("123") == None
    assert split_words("goya@gmail.com") == None
    assert split_words("Hello World!") == None
    assert split_words("Hello? World!") == None
``` 

The test suite covers various scenarios to ensure that the `split_words` function appropriately handles all edge cases. You can use these test cases to verify the functionality of the solution, ensuring it aligns with the problem's requirements and expectations.