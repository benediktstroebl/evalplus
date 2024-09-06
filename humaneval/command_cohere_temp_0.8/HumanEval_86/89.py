```python
def anti_shuffle(s):
    word_arr = []
    word_flag = False 
    ascii_flag = False

    for char in s:
        if char == " ":
            if word_flag:
                word_arr.append(char)
            else:
                ascii_flag = True
        elif char.isalpha():
            if ascii_flag:
                temp = ''.join(sorted(char))
                word_arr.append(temp)
                ascii_flag = False
            else:
                word_flag = True
        else:
            word_arr.append(char)

    return ' '.join(word_arr)
```

The function uses two flags to keep track of whether it is currently processing a word or an ASCII character. Using these flags, it sorts the characters within each word while keeping the order of words and spaces intact. This approach ensures that the relative positions of words and spaces in the string remain preserved while ordering the characters within each word.