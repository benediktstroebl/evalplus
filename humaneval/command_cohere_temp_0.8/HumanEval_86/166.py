```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (assuming words are separated by spaces) and then sorts the characters in each word based on their ascii values and finally joins them to produce the required 'ordered' version of the string.

Here is a test case that can be used to verify the functionality of the code:
```python
def test_anti_shuffle():
    # Case: Single word
    assert anti_shuffle("Hi") == "Hi"

    # Case: Multiple words
    assert anti_shuffle("hello world") == "ehllo ddlor"

    # Case: Long sentence with multiple words and special characters
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"
``` 

To further illustrate the function, let's break down the test case step by step:
1. Single word input: 'Hi'
    - The function splits this into the array: ['Hi']
    - Sorts ascii characters in 'Hi': ['H', 'i']
    - Returns original string: 'Hi'
2. Multiple words input: 'hello world'
    - The function splits this into the array: ['hello', 'world']
    - Sorts ascii characters in 'hello': ['e', 'h', 'l', 'o']
    - Sorts ascii characters in 'world': ['w', 'r', 'l', 'd']
    - Returns ordered string: 'ehllo ddlor'
3. Long sentence with multiple words and special characters input: 'Hello World!!!'
    - The function splits this into the array: ['Hello', 'World!!!']
    - Sorts ascii characters in 'Hello': ['H', 'e', 'l', 'l', 'o']
    - Sorts ascii characters in 'World!!!': ['W', 'r', 'd', 'l', 'o', '!!!']
    - Returns ordered string: 'Hello !!!Wdlor'

This demonstrates how the `anti_shuffle` function keeps the word order intact while sorting the characters within each word based on ascii values.