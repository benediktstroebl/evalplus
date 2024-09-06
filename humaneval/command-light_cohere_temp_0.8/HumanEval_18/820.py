```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string): 
            if char == substring)
    return 

# Example usage:
string = "aaaaaa"
substring = "aa"
print(how_many_times(string, substring)) # Output: 3
 ```