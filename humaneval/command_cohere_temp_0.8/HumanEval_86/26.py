```python
def anti_shuffle(s):
    word_list = s.split()
    new_word_list = []
    for word in word_list:
        ascii_sorted = ''.join(sorted(word))
        new_word_list.append(ascii_sorted)
    return ' '.join(new_word_list)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without altering the word order or whitespace. It splits the input string into individual words using whitespace as the delimiter. Then, for each word, it sorts its characters in ascending order based on their ASCII values and reassembles them into a new word. It then appends the newly sorted word to a list and returns the list joined by whitespace, leaving the word order intact, and thereby achieving the desired ordered version of the input string.

This code can be tested with the following inputs:
```python
print(anti_shuffle('Hi')) # Should return 'Hi'
print(anti_shuffle('hello')) # Should return 'ehllo'
print(anti_shuffle('Hello World!!!')) # Should return 'Hello !!!Wdlor'
``` 

Which would yield the following outputs:
```python
Hi
ehllo
Hello !!!Wdlor
``` 

However, this code employs a linear time sorting algorithm for a linear time problem, and hence can be further optimized. Here's an example using the `sorted` function which provides a more efficient implementation:
```python
def anti_shuffle(s):
    word_list = s.split()
    new_word_list = [sorted(word) for word in word_list]
    return ' '.join(new_word_list)
```

This version of the function utilizes Python's built-in `sorted` function to directly sort each word in the string. The anti_shuffle function still splits the input string into individual words and then applies the `sorted` function to each word, making it more efficient with a time complexity of O(n log n).