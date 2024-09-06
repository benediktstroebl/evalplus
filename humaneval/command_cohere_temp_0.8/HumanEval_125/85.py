```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split(' ')
    return words if words != ',' else len(list(filter(lambda c: ord(c) > 14 and ord(c) % 2 != 0, txt.lower())))
```

The problem gives a string of words and asks for the string to be split into a list of words. The list of words is returned if there are no spaces or commas in the string. If there are no spaces or commas, the function returns the number of letters with an odd character count. In the script provided, the `split_words` function splits the text on whitespace if there is a space in the text, and on commas if there are no spaces. It then returns this split as a list. If the list is , it returns the number of letters with an odd count, as described in the problem statement. 

Here is an example of how this code can be tested:
```python
# Test Splitting On Whitespace
assert split_words("Hello world!") == ["Hello", "world!"]

# Test Splitting On Comma
assert split_words("Hello, world!") == ["Hello", "world!"]

# Test With No Whitespace Or Commas
assert split_words("abcdef") == 3

# Test With Whitespace And Commas
assert split_words("Hello world!,abcdef") == ["Hello", "world!", "abcdef"]
```

The tests above test for different iterations of the problem statement to ensure that the `split_words` function is returning the correct value. 

Is there anything else I can help with?