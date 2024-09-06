```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This problem can be solved by parsing the string input with the split(' and '), converting the resulting strings into integers and subtracting them from the total number of fruits. The code exploits the fact that the given strings do not overlap in their elements and thus can be subtracted directly from the total number. 
This solution will cover test cases like "5 apples and 6 oranges", "0 apples and 1 oranges", "2 apples and 3 oranges", "100 apples and 1 oranges", etc.