```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    Args:
        word (str): The word to count consonants in.
    Returns:
        int: The number of consonants in the word.
    """
    count = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            count += 1
    return count

def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    Args:
        s (str): The input string.
        n (int): The number of consonants to filter by.
    Returns:
        list: A list of words from the string s that contain exactly n consonants.
    """
    words = s.split()  # Split the string into words
    filtered_words = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            filtered_words.append(word)

    return filtered_words
```

The `count_consonants` function is used to validate the input string `s` and calculate the number of consonants in each word. 

The `select_words` function splits the input string into individual words and then iterates through each word, checking if it matches the desired consonant count.

The code above adheres to the problem's assumption that the input string contains only letters and spaces. And returns an empty list if the input string is empty.

Here is an example usage of the above code:
```python
input_string = "Mary had a little lamb"
desired_consonant_count = 3

selected_words = select_words(input_string, desired_consonant_count)
print(selected_words)  # Expected output: ['Mary', 'lamb']
```

This should be the expected output, as these words contain 3 consonants. This aligns with the problem's example usage.