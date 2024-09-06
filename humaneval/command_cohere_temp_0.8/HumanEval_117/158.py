```python
def count_consonants(word):
    return sum(1 for char in word if char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

def select_words(s, n):
    words = [word for word in s.split()]
    words = [word for word in words if count_consonants(word) == n]
    return words
```
The `count_consonants` helps determine the number of consonants for a given word which is necessary for selecting the words with the desired consonant count. The `select_words` uses the list comprehension to select the words that have the specified number of consonants. The resulting solution is a list of words from the input string `s` that contain exactly `n` consonants in order of appearance. The solution handles the various edge cases like an empty string or not enough consonants in a word to fulfill the criteria. 
The overall time complexity of the code is `O(m * n)` where `m` is the number of words and `n` is the average length of the words in characters, and the space complexity is `O(n)` where `n` is the number of words. Do you need anything else to help further? 

## Offer Alternative Solution
If wanting an alternative approach, here's a solution using recursive descent:
```python
def select_words(s, n):
    def find_words(s, target, count):
        if not s:
            if target == count:
                return [s]
            return []
        if s[0].isalpha():
            consonant_word = find_words(s[1:], target, count) + [s[:1].lower()]
            return consonant_word + find_words(s[1:], target, count-1)
        else: 
            return find_words(s[1:], target, count)
    
    words = [word for word in s.split()]
    return find_words("", words, n)
```

This approach uses a recursive descent to generate all possible permutations of words in the input string `s` and checks which ones fulfill the criterion of having exactly `n` consonants. 

Let me know if you have any questions!