```python
def histogram(test):
    letters = test.strip().lower().split()
    histogram = {}
    for letter in letters:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram
```
The function uses a dictionary to store the letters of the alphabet and their corresponding counts. The function first strips away leading and trailing spaces from the input test string. It then converts the string to lowercase to ensure consistency in counting. Using the split() method, the function slices the string into separate letters and spaces, and then iterates through each letter to either increment its count in the histogram dictionary if the letter is already present, or add it with a count of 1 if it's encountered for the first time. The function returns the histogram dictionary containing the results.