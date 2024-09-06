Here's a Python script that defines a function `select_words()` to solve the problem you've described:
```python
def count_consonants(word):
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result

# Example usage:
input_string = "Mary had a little lamb"
n = 3
result = select_words(input_string, n)
print(result)  # Output: ["Mary", "lamb"]
```

This script will identify words in the `input_string` with exactly `n` consonants, and it will return those words as a list. 

The `count_consonants` function is used to calculate the number of consonants in a word, and is called before `select_words` to pre-process the word if a word is to be rejected due to having the incorrect number of consonants, this reduces the complexity of the `select_words` function. The script assumes that the input string contains only letters and spaces, as specified in the problem statement.