```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using space as a delimiter, iterates through each word, sorts the characters in ascending order based on their ASCII values, and then joins them back to produce the final ordered string.

Here is a sample output:
```python
print(anti_shuffle("Hello World!!!")) # Output: "Hello !!!Wdlor"
``` 

This approach provides a straightforward solution to the anti-shuffling problem, maintaining the order of words and spaces in the original string.