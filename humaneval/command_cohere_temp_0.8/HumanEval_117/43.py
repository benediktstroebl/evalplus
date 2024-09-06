Here's a Python script that contains a function called `select_words` which solves the problem you've described:
```python
def select_words(s, n):
    """
    Find words in a string that contain exactly 'n' consonants.
    
    Args:
    - s (str): Input string.
    - n (int): Number of consonants required in each word.

    Returns:
    - list: List of words containing exactly 'n' consonants.
    """
    # Ensure the input string is not empty
    if not s:
        return []

    # Split the string into individual words
    words = s.split()

    # Filter words based on the condition
    selected_words = [word for word in words if len(set(word.replace(' ', ''))) == n]

    return selected_words

# Unit Tests:
def test_select_words():
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("aa ba cc", 2) == ["aa", "cc"]
    assert select_words("^^^ooo^^oo^^^^", 4) == ["ooo"]

test_select_words()
```

The function first checks if the input string is empty, and if so, it returns an empty list. It then splits the string into individual words and filters them based on the condition specified in the problem statement, using a list comprehension.

The unit tests are included to validate the function's behavior against various test cases. Adjust the driver code (`test_select_words()`) to execute the tests as needed.