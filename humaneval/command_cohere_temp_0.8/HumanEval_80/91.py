```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as described in the problem statement. 

It first checks if the length of the string is at least 3, and if not, it returns `False`, since a string with fewer than 3 characters cannot be happy.

Then, it uses a set called `letters_set` to store the letters encountered as it iterates through the string. When iterating over the string with iterates of 3, it checks if the set of consecutive letters is of size 3, if not, it returns `False` as these consecutive letters are repeated. The function returns `True` if the string satisfies the criteria for being happy.

The code is structured as a self-contained function `is_happy` with a clear and concise implementation that directly tackles the problem. It avoids unnecessary complexity and is easy to understand.

To efficiently check if every 3 consecutive letters are distinct, it uses the technique of storing them in a set which automatically handles uniqueness.

The overall time complexity of this code is O(N), where N is the length of the input string, as it iterates through the string once and performs operations on each letter that typically take constant time.