```python
def count_consonants(word):
    consonants = 0
    for char in word:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u" and char.isalpha():
            consonants += 1
    return consonants

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` helper function calculates the number of consonants in a given word, while the `select_words` function splits the input string into words, iterates through each word, and retains those that have exactly `n` consonants.

Here's an example usage:
```python
input_string = "Mary had a little lamb"
n = 3

result = select_words(input_string, n)
print(result)  # Output: ["Mary", "lamb"]
```
This will output `["Mary", "lamb"]`, as both words have exactly 3 consonants.