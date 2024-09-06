```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    
    for i in range(n):
        if string[i] == substring:
            count += 1
        
    return count

# > how_many_times('aaaa', 'aa')
3
# how_many_times('abc', 'bc')
2
# how_many_times('xxx', 'xxy')
1
# how_many_times('abcde', 'ab')
0
```  This code defines a function that finds the count of a substring within a given string. It tests by iterating through character in the main string and checking if it's equal to the substring. It returns the number of occurrences of the substring.