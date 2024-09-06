```python
def match_parens(lst):
    def shift(s, offset):
        return s[:offset] + s[offset:]

    def calc_diff(a, b):
        return sum(1 for i, c in enumerate(a) if c != b[i])

    # If one string is empty, the other must be balanced
    if not lst[0]:
        return 'Yes'
    if not lst[1]:
        return 'Yes'

    # Split the strings into balanced chunks and calculate total offset
    chunks = []
    offset = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] == '(':
            if str2[i] == '(':
                offset += 1
            else:
                chunks.append(str1[i : i + 1])
        elif str2[i] == '(':
            chunks.append(str2[i : i + 1])
        else:
            if calc_diff(str1[i:], str2[i:]) != 0:
                return 'No'

    # Verify if the remaining chunks can form a balanced string
    if calc_diff(str1[offset:], str2) != 0 or calc_diff(str2[offset:], str1) != 0:
        return 'No'

    # Check if concatenating chunks with offset forms a balanced string
    concat = ''.join(chunks)
    if concat[offset:] == concat[:offset]:
        return 'Yes'
    return 'No'
```

The approach adopted in the function `match_parens` is to split the strings into balanced chunks and then calculate the offset required when concatenating these chunks. Finally, it checks if the concatenation of the chunks with the offset forms a balanced string. 

The function takes a list `lst`, which contains two strings consisting of open parentheses '(' or close parentheses ')' only. It checks if it is possible to concatenate the two strings in some order, such that the resulting string is balanced. The function returns 'Yes' if there is a way to make a good string, and 'No' otherwise.

The above approach has a time complexity of O(n^2) due to the nested loops, where n is the length of the string. It does not need further optimization due to the small input size constraint.