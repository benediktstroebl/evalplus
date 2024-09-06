```python
def anti_shuffle(s):
    word_arr = []
    word_flag = False 
    spaced = s.split(' ')
    for word in spaced:
      if word != '':
        word_arr.append(sorted(word))
        word_flag = True
      else:
        if word_flag:
          word_flag = False
          word_arr.append('')
    return (' '.join(map(str, word_arr)))
```

The code divides the input string s into a list of words, ensures the list's elements are sorted, and then returns the list as a space-separated string. It includes a flag to monitor the presence of words in the list and adds empty strings between words to maintain spacing. The approach efficiently resolves the anti-shuffle problem, ordering characters within words while maintaining word order and spacing in the original string.