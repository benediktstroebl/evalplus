```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This problem can be solved by parsing the string input with the split() method to obtain the number of apples and oranges. After converting these to integers, we simply subtract them from the total number of fruits to obtain the number of mangoes. Ultimately, our function returns this number of mangoes. 

If the given string is "XXX apples and YYY oranges" with N as the total number of fruits, this problem can be broken down into the following steps:
1. Parse the string to get the number of apples and oranges, let's call them A and O:
- A = number of apples
- O = number of oranges
2. Return N - A - O, this will be the number of mango fruits in the basket.