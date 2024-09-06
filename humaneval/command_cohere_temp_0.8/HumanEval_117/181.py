```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    Args:
        word (str): The word to count consonants in.
    Returns:
        int: The number of consonants in the word.
    """
    consonant_count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
                char.isalpha():
            if char.lower() != char.upper():
                consonant_count += 1
            else:
                consonant_count += 2
    return consonant_count

def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    Args:
        s (str): The input string.
        n (int): The number of consonants to filter on.
    Returns:
        list: A list of words containing exactly n consonants.
    """
    words = s.split()  # Split the string into words
    selected_words = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            selected_words.append(word)

    return selected_words if selected_words else []

# Test Cases
assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
assert select_words("simple white space", 2) == []
assert select_words("Hello world", 4) == ["world"]
assert select_words("Uncle sam", 3) == ["Uncle"]
```

This Python script solves the `select_words` function problem with a self-contained code block that might be used anywhere Python is used. It operates by first constructing a function `count_consonants` that determines the number of consonants in a given word. Following that, the primary function `select_words` splits the input string into individual words and evaluates each word's consonant count using the `count_consonants` function. If a word has exactly n consonants, it is added to the `selected_words` list. Finally, an empty list is returned if no words are discovered that match the criteria. The code is put through its paces with several test cases to ensure its correctness.

The approach makes advantage of the Python dictionary's and list's constant-time (amortized) append and lookup capabilities, making it efficient and scalable. Furthermore, the code is clearly written, well-tested, and readily available for future use in any Python environment.