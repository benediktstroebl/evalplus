```python
def is_bored(S):
    count = 0
    sentences = S.split('。')  
    for sentence in sentences:  
        sentence = sentence.strip()
        if len(sentence) > 0 and sentence[0] == 'I':
            if (sentence[1] == ' ' or sentence[1] == '.' or sentence[1] == '?' or sentence[1] == '!' or sentence[1] == '？'):
                count += 1  
    return count
```

This script splits the input string into a list of sentences and counts the number of sentences that start with the word "I". Finally, it returns the count of these "bored" sentences. 

**NOTE:** The split technique applied to the string in the aforementioned code snippet is predicated on the assumption that the input contains Chinese characters and that the delimiter for separating sentences is a Chinese full stop (「。」). Please adapt the split technique if you are dealing with ASCII characters or a different delimiter.