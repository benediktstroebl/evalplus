```python
def count_consonants(word):
    """
    Function to count the number of consonants in a word
    """
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct

def select_words(s, n):
    """
    Selects words from a string that contains exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        ct = count_consonants(word)
        if ct == n:
            result.append(word)
    return result
```
The above code contains two functions:
1. The `count_consonants` function accepts a word as input and calculates the number of consonants present in it.
2. The `select_words` function accepts a string and an integer `n` as input and returns a list of all the words contained in the string, which contain exactly `n` consonants.

The code works by first splitting the input string into individual words and then calculating the total number of consonants in each word using the `count_consonants` function. It then checks if the number of consonants in each word matches the provided number `n`, and if so, it includes that word in the result list. Finally, the function returns the list of selected words.

Here is an example of how to use the above code:
```python
input = "Mary had a little lamb"
n = 3
print(select_words(input, n))  # Output: ['Mary', 'lamb']
```
This would output `['Mary', 'lamb']` as these words contain 3 consonants.

This solution works for all the test cases as the total number of consonants in each word is calculated independently, and then it is compared to the input `n` to determine if the word qualifies for inclusion in the result set. 
  
 
```python
def count_consonants(word):
    """
    Function to count the number of consonants in a word
    """
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct
```
This function counts the number of consonants in a word. It does so by iterating through each character in the input word and checking if the character is a consonant. If it is, the consonant count (`ct`) is incremented. This function returns the final count of consonants.