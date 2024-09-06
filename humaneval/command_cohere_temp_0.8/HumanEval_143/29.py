```python
def words_in_sentence(sentence):
    sentence = sentence.split(' ')
    res = []
    for word in sentence:
      if len(word) in primes:
          res.append(word)
    return ' '.join(res)

primes = [i for i in range(2, 1000) if all(i % j for j in range(3, int(i**0.5)+1, 2))]
```

The provided code first splits the input sentence into individual words using space (' '), and then it iterates through each word in the sentence and checks if its length is a prime number. If the length of a word is prime, it gets appended to a list called "res". Finally, the function joins the words in the 'res' list back into a single string and returns the resulting string, which contains only the words whose lengths are prime numbers. The primes list is a precomputed list of prime numbers ranging from 2 to 999, created using a simple primality testing algorithm.