```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        char_array = list(word)
        char_array.sort()
        new_word = ''.join(char_array)
        new_word_array.append(new_word)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the words within the string, while maintaining the original word order and spaces. It does this by first splitting the input string into individual words and storing them in the `word_array` list. Then, it iterates through each word, converts it to a character array, sorts the characters in ascending order based on their ASCII values, and joins them back to create a new word. These new sorted words are stored in the `new_word_array` list. Finally, it returns a string where the newly created words replace the original words while keeping the word order and spaces intact.

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will create the ordered version of the string where each character is in ascending order based on its ASCII value while keeping the order of the words and spacing. 

This solution assumes that the input string might contain multiple words separated by spaces, and the function focuses on sorting the characters within each word while keeping the original word structure intact.