```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without changing the word order in the string. In the code, the input string is split into a list of words including blank spaces, and then an empty list `new_word_array` is initialized to store the sorted words. In the loop, each word is sorted based on ASCII values and appended to the `new_word_array`, and finally, the function returns a space-joined string of the sorted words.

Here is a simple test case to verify the code:
```python
print(anti_shuffle("Hi")) # Should return "Hi"
```

And here is a more complicated test case to make sure the code handles multiple words correctly:
```python
print(anti_shuffle("hello world")) # Should return "ehllo rdoll"
``` 

This ensures that the words "hello" and "world" are sorted alphabetically, while the order of the words remains unchanged.