```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        elif n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
        max_val = max(max_val, n)
    for n in freq:
        if freq[n] >= n:
            return n
    return -1
```

The function first creates a dictionary `freq` to store the frequency of each value in the list. It then iterates over the list, incrementing the frequency of each element and keeping track of the maximum value `max_val`.

After counting the frequencies, it checks each value's frequency, comparing it to the value itself. If a number has a frequency greater than or equal to its value, it returns that number. If no such number exists, it returns `-1`.

This solution utilizes basic dictionary and list comprehension operations, making it efficiently solve the problem in O(n) time complexity, where `n` is the length of the input list. 

The approach is logical and systematic, making it easy to understand and implement, and it delivers the desired result without any additional complexities.