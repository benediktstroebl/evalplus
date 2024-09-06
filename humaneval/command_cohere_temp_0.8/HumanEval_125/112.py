```python
def split_words(txt):
    ans = txt.split(',') if ',' in txt else txt.split() if ' ' in txt else len(list(filter(lambda c: ord(c) % 2, txt.lower())))
    return ans
```

The function takes an input string and checks if the string contains spaces or commas, and splits the string into a list of words. If the string contains none of these, it counts the number of lowercase letters with odd order in the alphabet. The function returns the list of words or the count of letters based on the above conditions. 

The total time complexity of the function is `O(n)`, where `n` is the length of the input string and the space complexity is `O(1)`, as the maximum additional space introduced by the function is constant, irrespective of the input size.