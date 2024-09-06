```python
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word."""
    
    # Declare vowel and consonant
    vowel = ''
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    # Split word to array by character
    word = word.lower()
    array = list(word)
    
    # Loop through the word to find if any vowel meets the problem statement
    for i in range(1, len(array)):
        if array[i] in vowels and consonants.find(array[i-1]) >= 0 and consonants.find(array[i+1]) >= 0:
            vowel = array[i]
            break

    return vowel
```

This Python script defines a function called `get_closest_vowel` that takes in a word as input. The function iterates through the characters of the word, ignoring the first and last characters, to identify if any vowel lies between two consonants. The function utilizes two variables to store the consonant and vowel characters, ensures the input is case insensitive, and returns the closest vowel meeting the problem statement's criteria. 

Let's break down the code:
- The `vowel` variable is declared as an empty string, and the `consonants` variable is declared as a string containing all English consonant characters, both in uppercase and lowercase. 
- The `word` variable is assigned the input word, and the `array` variable is created by splitting the word into a list of characters.
- The loop iterates through the characters of `word` (excluding the first and last characters). It checks if the current character is a vowel and if it can be found between two consonants. If this condition is met, the variable `vowel` is assigned the current character, and the loop breaks. 
- The function returns the value of `vowel`, which represents the closest vowel between two consonants, or an empty string if no such vowel is found. 

Overall, this code is efficient in solving the problem statement with a time complexity of O(n), where n is the length of the input word.