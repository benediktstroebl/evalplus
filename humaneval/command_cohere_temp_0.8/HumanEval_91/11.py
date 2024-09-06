```python
def is_bored(S):
    count = 0
    words = S.split()
    for i in range(len(words)):
        if words[i] == 'I':
            j = i + 1
            while j < len(words):
                if words[j] == '.' or words[j] == '?' or words[j] == '!':
                    break
                j += 1
                if j > i + 2 and (words[i + 1] == 'am' and words[i + 2] == 'boring') or \
                   (words[i + 1] == 'was' and words[i + 2] == 'boring') or \
                   (words[i + 1] == 'is' and words[i + 2] == 'boring'):
                    count += 1
                    break
                j += 1
    return count
```

Let's break down the Python solution provided:
1. **Function Definition**: 
   - `def is_bored(S)`: This line defines a function named `is_bored` that takes a single argument `S`, which is the input string.
2. **Boredom Detection**:
   - `count = 0`: Initializes a counter to keep track of the number of boredoms in the input string.
   - `words = S.split()`: Splits the input string into a list of words by splitting at spaces. This allows us to iterate over each word easily.
   - `for i in range(len(words))`: Iterates through each word in the list.
   - `if words[i] == 'I'`: Checks if the current word is 'I', which marks the start of a sentence.
3. **Sentence Parsing**:
   - `j = i + 1`: Sets the variable `j` to iterate through the words starting from the next word after 'I'.
   - The loop continues until it reaches a sentence delimiter (`.`, `?`, or `!`).
   - Inside the loop, it checks for various patterns to detect boredom. The conditions are grouped with parentheses and the logical `OR` (`||`) operator to ensure that any match is counted.
   - `if j > i + 2 and (words[i + 1] == 'am' and words[i + 2] == 'boring') or ...`: These conditions check for different ways of saying "I am boring" and "I was boring" in various tenses, to capture different ways people might express boredom. 
4. **Count Update**:
   - If a boredom is detected, `count` is incremented. 
   - The loop continues to the next word if it's not a sentence delimiter.
5. **Return Result**:
   - After iterating through all words, the function returns the total count of boredoms.

This solution efficiently counts boredoms in the given input string by parsing sentences and checking for different patterns that indicate boredom. It provides a clear and concise way to solve this problem.