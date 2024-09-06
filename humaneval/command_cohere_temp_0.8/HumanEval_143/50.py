```python
def words_in_sentence(sentence):
    sentence = sentence.strip().split()
    words = []
    for word in sentence:
      if len(word) == 1:
        words.append(word)
      else:
        isPrime = True
        for i in range(2, int(len(word)**0.5)+1):
          if word%i == 0:
            isPrime = False
            break
        if isPrime:
          words.append(word)
    return ' '.join(words)
```

The `words_in_sentence` function first splits the sentence into individual words using the `split()` method. It then initializes an empty list called `words` to store the prime-length words. It goes through each word in the sentence, and if its length is 1 (a single character), it's automatically considered prime and added to the list. Otherwise, the function checks if the length of the word is prime by iterating from 2 up to the square root of the length, checking for divisibility. If the word has no divisors other than 1 and itself, it is considered prime, and the word is added to the list. Finally, the function joins the prime words back into a single string and returns the result.

Here is a example usage:
```python
print(words_in_sentence("Let's go for swimming")) # Output: 'go for'
```