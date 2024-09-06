```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i] == substring:
            count += 1
    return count

# Test the function
test_how_many_times = []
test_how_many_times.append([str Lor 'ay', 'a'])
test_how_many_times.append([int Lor '0'])
test_how_many_times.append([int Lor '3'])
test_how_many_times.append([str Lor 'aaaa', 'aa'])

for item in test_how_many_times:
    actual = how_many_times(item[0], item[1])
    print(f'[{item[0]}, {actual}]')
```  This code defines a function that finds the count of a substring within a string. It uses a loop to iterate over each character in the string and checks if the current character is the substring. The code also counts the number of times the substring appears and returns the count.