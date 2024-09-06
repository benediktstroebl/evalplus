```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(zip(s[:3], s[1:4], s[2:5]))
    return not any(map(lambda x: len(set(x)) == 1, letters_set))
```

The function uses a clever approach to efficiently check if the string is happy. It utilizes the fact that any 3 consecutive letters in a happy string must form a set of 3 distinct elements. It uses `zip` to group the consecutive letters and then checks if any of these groups have only one unique element, which would indicate that the 3 consecutive letters are not distinct. 

The overall time complexity of the function is O(n) where n is the length of the input string s, and the space complexity is O(1) as it only uses a constant amount of extra space to manipulate the input string. 

Note that the original problem statement did not have a constraint on the length of the string, however, for the purpose of this problem, it is reasonable to assume that a happy string must have a length of at least 3 to be happy.