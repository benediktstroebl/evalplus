```python
def number_of_odd_digits(string_list):
    r = []
    for s in string_list:
        a = sum(1 for c in s if c % 2 == 1)
        b = str(a)
        b2 = b.replace('1', 'n')
        b3 = b2.replace('0', 'o')
        b4 = b3.replace('3', 'w')
        b5 = b4.replace('2', 'u')
        r.append(b5)
    return r
```

The function iterates through each string in the list and counts the number of odd digits using a generator expression. Then, it creates a string with the odd digit count and subsequently replaces specific digits with relevant words to form a grammatically correct sentence. This sentence is then added to the list r, which is returned. 

Such a strange task can be a piece of a more extensive puzzle, such as a software test or a code interview question. If you want to elaborate on this problem or have any other questions, please let me know! I can create additional scripts or problems to practice various coding concepts and puzzles. Let me know if you are preparing for something specific and I can try to accommodate you.