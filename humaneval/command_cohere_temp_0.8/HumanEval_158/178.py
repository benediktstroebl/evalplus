```python
def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for w in words:
        uniq = len(set(w))
        if uniq > max_uniq:
            max_uniq = uniq
            result = w
    return result
```

The function uses a simple algorithm. It first sorts the words list in lexicographical order. Then, it iterates over each word, calculating the number of unique characters in each word and updating the maximum count and the corresponding result. Once the loop is finished, the result variable will hold the word with the maximum number of unique characters.

Here is a more detailed explanation of the algorithm for better understanding:
- Sort the input list of words alphabetically. This step is essential for the subsequent steps.
- Initialize the 'max_uniq' variable to 0. This variable will store the maximum number of unique characters encountered.
- Initialize the 'result' variable as None. This variable will store the word with the maximum number of unique characters.
- Iterate over each word in the sorted list.
    - Calculate the number of unique characters in the current word. It is done using the 'len(set(word))' function. The 'set' function converts the word into a set of characters, and the length of this set gives the number of unique characters.
    - If the number of unique characters is greater than the current maximum ('max_uniq'), update both 'max_uniq' and 'result'. 'result' is updated to the current word as it is the new winner in terms of the maximum number of unique characters.
- Once the loop is finished, the 'result' variable will hold the word that has the maximum number of unique characters. Return this word.

The algorithm has a time complexity of O(n log n) due to the sorting step, and an additional O(n) due to the iteration over the words. The space complexity is O(1) as it only uses variables to store the current word and the maximum unique value. No extra space is used to store the entire words list or any additional data. Note that the words list is modified by the algorithm, but this is an essential step to run the correct function, as stated in the problem statement. Overall, the function is efficient and well-designed to solve the problem.