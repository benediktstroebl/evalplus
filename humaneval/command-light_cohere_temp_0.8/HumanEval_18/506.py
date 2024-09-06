```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Example usage
string = "aaaaaa"
substring = "aa"
count = how_many_times(string, substring)
print(f"{count} times substring '{{substring}}' can be found in the original string.")
 ```