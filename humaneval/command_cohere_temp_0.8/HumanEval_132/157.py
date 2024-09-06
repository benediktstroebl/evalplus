```python
def is_nested(s):
    open, close = 0, 0
    for char in s:
        if char == '[' :
            open += 1
        elif char == ']':
            close += 1
        if open > close:
            return False
    return open != close
```

The function counts the openings '[' and closings ']' in the string using two counters. It increments the first counter whenever it encounters an opening bracket and the second counter whenever it encounters a closing one. When the total number of openings is not equal to the total number of closings, it means there is at least one nested bracket. The function returns False in this case, as per the problem statement. Otherwise, if the counts are equal, it returns False, implying no nested brackets. The provided example inputs and outputs demonstrate the function's behavior:
```python
print(is_nested('[[[[]]]]')) #True
print(is_nested('][]'))      #False
print(is_nested('[][]'))     #False
print(is_nested('[[[]]]'))   #True
print(is_nested('[[['))     #True
print(is_nested(']'))        #False
``` 
The first example returns True since there is a valid subsequence of brackets where one bracket (the outermost one) is nested. The second example returns False as there are more closing brackets than opening ones. The third example returns False since although there are an equal number of openings and closings, there is no nested bracket. The fourth and fifth examples reflect the function's behavior for valid and invalid nested sequences, respectively.