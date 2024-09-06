```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This Python code defines a function named **`how_many_times`** that aims to determine the frequency of a given substring within a given string. The function utilizes the search.

Here's the explanation of the code:
- The function **`how_many_times`** takes two parameters: **`string`** and **`substring`**.
- It utilizes the **`find`** method from Python's string module to search for occurrences of the substring within the original string. 
- The **`find`** method returns an iterator yielding match locations. By using the particular index, the function calculates the total count of occurrences of the substring.
- This approach is both efficient and straightforward for this specific problem.