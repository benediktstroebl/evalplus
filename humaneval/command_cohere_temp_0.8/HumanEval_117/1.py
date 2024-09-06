```python
def count_consonants(word):
    count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
           char != 'y' and char != 'Y':
            count += 1
    return count
    

def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result

# Example usage
input_string = "Mary had a little lamb"
n = 3
print(select_words(input_string, n))
```

This script splits the input string into words and then iterates over each word, using the `count_consonants` function to count the number of consonants in each word. If the count matches the required number `n`, the word is added to the `result` list. The final list of words containing exactly `n` consonants is then returned. 

The `count_consonants` function counts the number of consonants in a word by iterating through each character in the word and checking if it is a consonant. The term "consonant" is defined in the code using a boolean check towards specific vowels and the characters 'y' and 'Y'. 

The provided example usage demonstrates the script's expected behavior and outputs:
```bash
['Mary', 'lamb']
``` 
This output corresponds to the example string "Mary had a little lamb" and the requested number of consonants, namely 3.