```python
def is_bored(S):
    count = 0
    words = S.split()
    for i in range(len(words)):
        if words[i] == 'I':
            if i + 2 < len(words) and (words[i + 1] == '.' or words[i + 1] == '?' or words[i + 1] == '!'):
                count += 1
    return count
```

This approach divides the string of words into a list of individual words and then iterates through each word to find sentences starting with "I" and ending with a punctuation mark. When such a sequence is found, it increments the count variable. Finally, the function returns the variable count, which stores the total count of boredoms. 

This solution adheres to the problem description, providing a precise and efficient way to determine the number of boredoms within a given input string.