```python
def words_in_sentence(sentence):
    sentence = sentence.split(' ')  # split the sentence into array of words
    prime_words = []  # array to store prime number words
    for word in sentence:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)  # add the word to the prime_words array
    return ' '.join(prime_words)  # return a string of words with prime number lengths

def is_prime(n):  # check if n is prime
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Driver Code
sentence = "this is a test"
print(words_in_sentence(sentence))  # Output: is

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Output: go for
```

This script first splits the sentence into a list of words, then uses the `is_prime` function to check if the length of each word is prime, and finally joins the prime words back into a sentence.

The `is_prime` function checks whether the given number n is less than or equal to 1, in which case it returns False, and if not, it iterates through the numbers from 2 to `int(n**0.5) + 1` (roughly the square root of n) and checks whether n is divisible by any of them, if `n` is divisible by any of them it returns False, otherwise it returns True.