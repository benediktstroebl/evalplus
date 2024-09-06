```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (uppercase or lowercase)
    or the hyphen ('-').
    """
    consonants = 0
    for char in word:
        if char.isalpha():
            if char in 'QWERTYUIOP{}|':
                consonants += 1
        elif char == '-':
            consonants += 1
    return consonants

def select_words(s, n):
    """
    This function selects words from a string that contain exactly 'n' consonants.
    If the string is empty or the number of consonants is less than 'n',
    an empty list is returned.
    """
    words = []
    word_args = [s.split(' ')]
    for i in range(len(word_args[0])):
        word = word_args[0][i]
        if count_consonants(word) == n:
            words.append(word)
    return words

# Test Cases
def test_select_words():
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("Pen-Island", 2) == ["Pen-Island"]
    assert select_words("Extraordinary", 5) == ["Extraordinary"]
    assert select_words("", 5) == []

test_select_words()
```

The above code contains two functions:
1. `count_consonants(word)`: This function counts the number of consonants in a given word. It checks each character of the word and increments a counter if it is a consonant. The definition of a consonant here is a letter that is not a vowel (uppercase or lowercase) or the hyphen ('-').
2. `select_words(s, n)`: This function selects words from a string `s` that contain exactly 'n' consonants. It splits the input string into words and iterates over them. For each word, it checks if the count of consonants is equal to 'n' using the `count_consonants` function. If true, it adds the word to a list, which is returned finally. If the string is empty or the number of consonants is less than 'n', it returns an empty list.

Both functions are then tested using the `test_select_words()` function. You can use this code by copying and pasting it into a Python environment of your choice.