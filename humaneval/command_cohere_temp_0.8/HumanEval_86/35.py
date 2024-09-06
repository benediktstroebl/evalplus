```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This code defines a function `anti_shuffle` that takes a string as input and returns a sorted version of the words within the string, retaining the order of words and spaces. It accomplishes this by first splitting the input string into individual words using spaces as separators. Then, for each word, it creates a new word by sorting the characters in ascending order based on their ASCII values and joining them together. These sorted words are stored in the `new_word_array`. Finally, the function returns the original string with the sorted words, maintaining the word order and spaces. 

The code is encapsulated in a self-contained function, making it modular and easy to use. When provided with a string, the function returns the desired ordered version of the string as described in the problem statement.