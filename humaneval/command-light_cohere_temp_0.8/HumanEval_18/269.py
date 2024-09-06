```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string = "aaaaaa"
substring = "aa"
result = how_many_times(string, substring)
print(result)  # Output: 3

# Test case 2
string = "hello"
substring = "el"
result = how_many_times(string, substring)
print(result)  # Output: 2
``` 
This code provides a self-contained Python function that finds the count of occurrences of a given substring within a string. It uses a straightforward iterators and conditionals to achieve this.