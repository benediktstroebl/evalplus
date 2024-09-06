```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0

    while start < len(string):
        count += string[start] == substring
        start += 1

    return count

#Tests
def test_how_many_times():
    assert how_many_times("aaa", "a") == 3

def main():
    print(how_many_times("sample text", "sample"))

if __name__ == "__main__":
    main()
``` 
The function **how_many_times** returns the number of times a given substring can be found in the original string. The function uses a strategy of looping through the original string and counting occurrences. It is well-contained and optimized to solve the given problem.