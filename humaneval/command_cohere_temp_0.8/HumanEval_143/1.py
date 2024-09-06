```python
def words_in_sentence(sentence):
    sentence = sentence.split(' ')
    prime_words = []
    for word in sentence:
      if is_prime(len(word)):
        prime_words.append(word)
    return ' '.join(prime_words)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This code divides the sentence into individual words using `split(' ')`, initializes an empty list called `prime_words` to store prime-length words, and then iterates through each word in the sentence using a for loop. The `is_prime` function is used within the loop to determine if the length of each word is a prime number. If it is, the word is added to the `prime_words` list. Finally, the function joins the prime words back into a single string and returns the result.

This solution works by:
1. Testing primality of lengths using `is_prime` function.
2. Including words in the output if their lengths are prime.

It ensures that only words with prime lengths are extracted from the sentence and combined without consideration of the original word orders.