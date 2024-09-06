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

This Python script defines a function `search` to solve the problem. It iterates through the list, maintaining a dictionary `freq` to track the frequency of each integer, and updates `max_val` as it progresses. After tallying the frequencies, the function checks if any integer has a frequency greater than or equal to its value, returning it if found. If no such integer exists, it returns -1. 

The code is self-contained and can be easily copied and run as a standalone script to test or use in other projects. 
This solution works because the code maintains the frequency of elements in the list and then compares this frequency to the value of the number itself. This allows it to identify the number that satisfies the condition of having a frequency greater than or equal to its own value, or to determine that no such number exists in the list, thus returning -1. Mention: The markdown code block has been omitted to make the response more concise, but this code can still be copied and run as a standalone Python script as wanted.  If needed, the markdown code block can be added again.