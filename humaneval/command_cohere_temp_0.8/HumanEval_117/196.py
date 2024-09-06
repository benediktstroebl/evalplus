Here's a Python script that contains a function to solve the problem you've described:
```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    """
    consonant_count = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonant_count += 1
    return consonant_count

def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    """
    words = s.split()
    selected_words = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            selected_words.append(word)

    return selected_words if selected_words else ["None"]

# Example usage
input_string = "Mary had a little lamb"
n = 3
result = select_words(input_string, n)
print(result)
```

This script includes two functions. The `count_consonants` function calculates the number of consonants in a given word, while the `select_words` function takes an input string and counts the number of consonants in each word. It then selects and returns all words containing exactly 'n' consonants. 

When you run the code, it will produce the following output:
```bash
['Mary', 'lamb']
```

This code demonstrates a practical application of Python for problem-solving, manipulating strings, and implementing algorithms to find specific words based on consonant counts.