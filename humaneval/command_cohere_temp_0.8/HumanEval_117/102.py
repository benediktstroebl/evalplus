```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total

def select_words(s, n):
    """Return list of words containing exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        count = count_consonants(word)
        if count == n:
            result.append(word)
    return result
```
The approach works by first creating a new list of words by splitting the input string s using spaces as separators. Then, we iterate through each word using a for loop. For each word, we use the previously defined helper function count_consonants to count the number of consonants in the word. If the count equals n, we append the word to the result list. Finally, we return the result list. 

The helper function count_consonants takes a word as input and returns the number of consonants present in the word. Let's break down its functionality:
- word = word.lower(): The function first converts the input word to lowercase to ensure case-insensitive counting.
- total = 0: Initializes a counter variable total to keep track of the number of consonants.
- for char in word: iterates through each character in the word.
- if char in "bcdfghjklmnpqrstvwxyz": counts the consonant characters. The variable char is checked against each consonant letter in the alphabet. If it matches, it increments the total count.
- return total: Returns the final count of consonants. 

This approach solves the problem efficiently and elegantly, splitting the string and counting consonants using a loop and helper function. The markdown code block can provide a concise and readable solution to the problem statement. Feel free to ask any questions or further clarifications!