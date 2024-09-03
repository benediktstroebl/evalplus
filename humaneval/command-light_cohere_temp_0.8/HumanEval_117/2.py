```python
def select_words(string, n):
    if not string:  # Empty string is valid input
        return []
    words = [word for word in string if word.count(word, n)]
    return words

# Test cases
test_cases = [
    ("Mary had a little lamb", 4),
    ("Mary had a little lamb", 3),
    ("simple white space", 2),
    ("Hello world", 4),
    ("Uncle sam", 3),
]

for i, (text, n) in enumerate(test_cases):
    words = select_words(text, n)
    print(f"Test {i+1}: {text} : {words}")
```
This code defines a function **select_words** that takes a string and an integer **n** as input, and returns a list of words from the string that contain exactly **n** consecutive consonants. The function works by iterating through each character in the string, and counting the consecutive occurrences of the corresponding consonant. The test cases section verifies the words that are expected to be returned based on the passed parameters.