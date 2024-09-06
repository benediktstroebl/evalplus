```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts a string and a substring as inputs and returns the number of times the substring occurs in the string, including cases of overlapping. It achieves this using the built-in `count()` method of Python strings. This method returns the number of times a given substring occurs within the string, without distinguishing between overlapping and non-overlapping occurrences. 

Such a simple solution is applicable because the problem statement explicitly states that overlapping cases should be counted. If the issue had requested non-overlapping cases exclusively, a more complex solution involving parsing would be required. 

This solution is efficient in terms of time complexity, with a linear time cost proportional to the length of the input `string` (`O(n)`). This makes it an effective solution for large and small contexts alike.

In terms of memory complexity, as it utilizes the built-in `count()` method, the algorithm is constant with respect to the substring length (`O(1)`). Thus, the function's efficiency is primarily dependent on the length of the input string. This memory efficiency implies that the function's performance does not significantly depend on the complexity of the substring input. 

Overall, the given solution is effective for the stated problem, providing both a straightforward implementation and efficient performance.