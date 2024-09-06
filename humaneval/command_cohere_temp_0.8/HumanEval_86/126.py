```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string, where each word is sorted based on ASCII values. The function first splits the input string into individual words using the `split()` method. Then, it iterates over each word, sorting the characters in alphabetical order and creating a new word from the sorted characters. Finally, the function joins the newly sorted words back together with spaces in between to form the final output string.

To verify the correctness of the solution, it can be tested with the following inputs:
```python
print(anti_shuffle('Hi')) # Should return 'Hi'
print(anti_shuffle('hello')) # Should return 'ehllo'
print(anti_shuffle('Hello World!!!')) # Should return 'Hello !!!Wdlor'
``` 
which all yield the expected output. Feel free to ask any questions or provide any additional feedback!