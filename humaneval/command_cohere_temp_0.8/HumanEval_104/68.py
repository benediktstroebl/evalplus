```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c not in '02468')) for i in x if int(''.join(c for c in str(i) if c not in '02468')) == i]
    return sorted(odd)
```
```
The function unique_digits processes each integer in the input list x as follows:
1. Converts the integer to a string,
2. Removes all even digits ('0', '2', '4', '6', '8') from the string,
3. Converts the modified string back to an integer, and
4. Checks whether the modified integer is equal to the original integer.

This ensures that the resulting integer equals the original integer unchanged if it does not contain any even digits. The function then collects these modified integers in the list odd and returns the list sorted in ascending order.
```
This solution has a time complexity of O(n log n) due to the sort operation on the result list. However, the solution is inefficient with a time complexity of O(n^2) for integers with many digits. It also has an auxiliary space complexity of O(n).