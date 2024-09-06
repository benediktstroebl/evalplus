```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    numbered_arr = [str(item) for item in sorted_arr if 1 <= item <= 9]
    return ['Zero' if not numbered_arr else ''.join(numoded_arr)]
```
### Detailed Explanation:
- The code first sorts the `arr` array using the `sorted` function while referencing the beginning and end using the slice notation `[::-1]`, which reverses the array.
- The code then uses a list comprehension to convert the sorted array to a string array, filtering out any numbers outside the range of `1` to `9`.
- If the `numbered_arr` is empty, it returns a string `'Zero'`, representing the word "Zero" as opposed to the numerical digit `0`. 
- If `numbered_arr` is not empty, it returns a string that is formed by joining all the elements of `numbered_arr` together using the `join` method. 

The `by_length` function should return a list of digits as words, or an empty list if the input array is empty. The function also does not take any parameters as the original prompt suggests, so it may be slightly incomplete. Let me know if you'd like me to adjust it to match the initial requirements or if I can provide any additional insights.