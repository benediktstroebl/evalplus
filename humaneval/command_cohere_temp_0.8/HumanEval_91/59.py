```python
def is_bored(S):
    cnt = 0
    for line in S.splitlines():
        line = line.strip() 
        if line.startswith("I ") and (line.endswith(".") or line.endswith("?") or line.endswith("!")): 
            cnt += 1
    return cnt
```
This Python script defines a function called `is_bored` that takes a string as an input parameter named `S`. The function counts the number of boredoms in `S`. A boredom is defined as a sentence that starts with the word "I" and ends with either a period, a question mark, or an exclamation mark. The function splits the input string into lines, iterates through each line, and checks if it starts with "I " and ends with a period, question mark, or exclamation mark. If these conditions are met, it increments the count of boredoms by 1. Finally, the function returns the total count of boredoms in the input string.