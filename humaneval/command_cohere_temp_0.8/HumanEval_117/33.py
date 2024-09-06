```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                cnt += 1
    return cnt

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
```
The provided Python script solves the problem by first creating a helper function **count_consonants(word)** that calculates the number of consonants in a given word. It traverses each character in the word and if it's a letter (thus excluding 'a', 'e', 'i', 'o', and 'u'), it counts it as a consonant. 

The main function **select_words(s, n)** splits the input string into a list of words and then iterates through each word, checking if the count of consonants matches the desired count 'n'. If so, the word is added to the **result** list. The final output is the list of words from the input string containing exactly 'n' consonants, in their respective order.

This solution has a time complexity of O(n + m), where 'n' is the number of words and 'm' is the maximum length of a word, which makes it efficient for most inputs. It also uses constant space for the 'result' list and for maintaining a consonant count for each word.