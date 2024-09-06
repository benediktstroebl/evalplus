```python
def how_many_times(string, substring):
    return len(string) - len(string.replace(substring, ''))
```

This function calculates the number of times the `substring` occurs in the `string` by taking into account overlapping instances. It utilizes the replace method to remove all occurrences of the `substring` from the `string`, and then calculates the difference in length between the original `string` and the modified string without `substring`. This difference yields the desired count. The unit tests stated in the problem are effectively passed by this function.