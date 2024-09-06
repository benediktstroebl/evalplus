```python
def count_consonants(word):
    cnt = 0
    for char in word:
        if char.lower() in 'bcdfghjklmnpqrstvwxyz':
            cnt += 1
    return cnt

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        cnt = count_consonants(word)
        if cnt == n:
            result.append(word)
    return result
```
The provided Python script implements the `select_words` function, which takes a string `s` and an integer `n` as inputs. This function returns a list of all words from the string `s` that contain exactly `n` consonants, in the order they appear in the string. 

To achieve this, the script first defines a helper function `count_consonants(word)` that calculates the number of consonants in a given word. It iterates through each character in the word and checks if the lowercase version of the character is a consonant. The count is incremented if the character is a consonant.

The `select_words` function first splits the input string `s` into a list of words using the `split()` method. It then iterates through each word in the list and calculates the number of consonants using the `count_consonants` function. If the count is equal to the specified number `n`, the word is added to the `result` list.

The script handles the edge case where the input string is empty by returning an empty list, as stated in the problem statement. Additionally, the examples provided in the problem statement are tested and the corresponding expected outputs are returned by the function.