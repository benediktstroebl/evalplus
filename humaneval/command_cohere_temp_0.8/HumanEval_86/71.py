```python
def anti_shuffle(s):
    word_list = s.split()
    new_word_list = []
    for word in word_list:
        new_word = ''.join(sorted(word))
        new_word_list.append(new_word)
    return ' '.join(new_word_list)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the words within the string, while maintaining the order of words and spaces. It accomplishes this by first splitting the input string into a list of words. Then, for each word in the list, it sorts the characters alphabetically, and rejoined them to create a new word. These new words are stored in a new list and returned as a space-separated string.

This approach ensures that the original structure of the input string is preserved, while rearranging the characters within each word. 

To test this function, you can use the following inputs:
```python
print(anti_shuffle('Hi')) # Should return 'Hi'
print(anti_shuffle('hello')) # Should return 'ehllo'
print(anti_shuffle('Hello World!!!')) # Should return 'Hello !!!Wdlor'
``` 
If the function is implemented correctly, it should return the ordered versions of the strings as mentioned above.