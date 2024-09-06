Here's a Python script that defines a function `select_words()` to solve the problem:
```python
def count_consonants(word):
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
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

# Example usage
input_string = "Mary had a little lamb"
n = 3
result = select_words(input_string, n)
print(result)
```

The `count_consonants` function is introduced to calculate the number of consonants in a given word, which is necessary for solving this problem. The main `select_words` function splits the input string into a list of words, iterates through each word, and checks if its consonant count matches the specified `n`. Words meeting this requirement are appended to the `result` list. The example usage demonstrates how to call the function with an input string and a desired number of consonants.