```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    
    for i in range(n):
        if string[i] == substring:
            count += 1
    
    return count

#Tests
string1 = "aaaa"
assert how_many_times(string1, string1) == 3

string2 = "abc"
assert how_many_times(string2, string2) == 1

string3 = "hello"
assert how_many_times(string3, string3) == 0

``` 
This function uses a for loop to iterate over every character in the string. It counts if the each character matches the number of times the substring appears in the string is returned.