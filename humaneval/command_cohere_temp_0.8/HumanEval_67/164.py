```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This problem can be solved by parsing the given string with the split(' and ')) method to obtain the number of apples and oranges. After converting these elements to integers, we perform simple subtraction to find the missing value to obtain the number of mangoes. The final result will be the total number of fruits in the basket minus the number of apples and oranges.