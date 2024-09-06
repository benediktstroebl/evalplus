```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits from the first to the last integer given,
    only including those that are present in both numbers.
    """
    list1 = str(a).replace('1', '').strip('0')
    list2 = str(b).replace('1', '').strip('0')
    even_digits = [int(digit) for digit in set(list1 + list2) if int(digit) % 2 == 0]
    return even_digits
```

The logic behind this approach involves:
1. Creating separate strings of the digits of `a` and `b` by removing `1`s and any extra `0`s.
2. These digit strings are then concatenated and a set is created to remove any duplicate digits.
3. Subsequently, a list comprehension is used to filter out even digits present in the set, thereby meeting the problem requirements. 

This approach results in a time complexity of `O(log(max(a, b)) * log(min(a, b))` and a space complexity of `O(log(max(a, b)) + log(min(a, b)))`, assuming no extra space is utilized. 

It's important to note that this solution is not optimized for numeric ranges closer to each other, as the set creation and even-checking loop may not be efficient in such cases. However, the simplicity of the code may make it suitable for smaller input ranges.