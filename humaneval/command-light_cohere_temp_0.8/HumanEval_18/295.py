```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while not overlapping. 
    """
    string = string.replace(substring, 'a', 0) 
    return sum(1 for i,c in zip(string, substring))

# Example 
Someting 'hello' in 'world' world...: 5
string = 'world' #replace('hello', 'o') 
substring = 'hello'
result = how_many_times(string, substring)
print(result) # 5

# Test case 2
string = 'aa'aa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaa'aaaa'aaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaa'aaaaaaaaaaa'aaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaa'aaaaaaa'aaaa'aaaa'aaaaaaaaaaa'aaaa'aaaa'aaaaaaaa'aaaa'aaaa'aaaaaaa'aaaa'aaaa'aaaaaaa'aaaa'aaaaaaaaaaa'aaaa'aaaa'aaaaaaa'aaaa'aaaa
substring = 'aa'aaaaaaa'aaaaaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaaaaa'aaaa'aaaaaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaaaaa'aaaa'aaaaaaa'aaaa'aaaaaaa'aaaaaaa'aaaa'aaaaaaaaaaa'aaaaaaa'aaaa'aaaaaaa'aaaaaaaa'aaaa....
result = how_many_times(string, substring)
print(result)  # 3
```